#!/usr/bin/env python3
from __future__ import annotations
import argparse, datetime as dt, json, re, sys
from pathlib import Path
from typing import Any
try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML required: python -m pip install -r tools/requirements.txt") from exc

ROOT = Path(__file__).resolve().parents[1]
CFG = {
 "DEC":{"recordType":"DECISION","folder":"decisions","statuses":{"DRAFT","PENDING_INPUT","DECIDED","EXECUTING","REVIEW_DUE","CLOSED","SUPERSEDED"}},
 "EXC":{"recordType":"EXCEPTION","folder":"exceptions","statuses":{"PROPOSED","APPROVED","ACTIVE","REVIEW_DUE","EXPIRED","REVOKED","INCORPORATED_INTO_STANDARD"}},
 "RSK":{"recordType":"RISK_ACCEPTANCE","folder":"risks","statuses":{"PROPOSED","ACCEPTED","MITIGATING","MONITORING","REVIEW_DUE","CLOSED","REVOKED"}},
 "DSS":{"recordType":"PROFESSIONAL_DISSENT","folder":"dissent","statuses":{"RECORDED","ACKNOWLEDGED","RESOLVED_BY_DECISION","SUPERSEDED_BY_NEW_EVIDENCE","WITHDRAWN_BY_AUTHOR"}},
}
TYPE2PREFIX={v["recordType"]:k for k,v in CFG.items()}
CONF={"PUBLIC","INTERNAL","RESTRICTED","LEGAL_CONFIDENTIAL","PEOPLE_CONFIDENTIAL"}
MAT={"M0","M1","M2","M3","M4","HARD_STOP"}
ID_RE=re.compile(r"^(DEC|EXC|RSK|DSS)-(\d{4})-(\d{3,})$")

def files():
    out=[]
    for c in CFG.values():
        p=ROOT/"records"/c["folder"]
        if p.exists(): out += list(p.glob("*.yaml"))+list(p.glob("*.yml"))
    return sorted(set(out))

def load(p):
    with p.open(encoding="utf-8") as f: return yaml.safe_load(f)

def date(v):
    if isinstance(v,dt.datetime): return v.date()
    if isinstance(v,dt.date): return v
    if isinstance(v,str):
        try:return dt.date.fromisoformat(v)
        except ValueError:return None
    return None

def nonempty(v):
    if v is None:return False
    if isinstance(v,str):return bool(v.strip())
    return True

def finding(sev,code,rid,msg,path): return {"severity":sev,"code":code,"recordId":rid,"message":msg,"path":path}

def validate(today=None):
    today=today or dt.date.today(); recs=[]; fs=[]
    for p in files():
        rel=str(p.relative_to(ROOT))
        try:d=load(p)
        except Exception as e:
            fs.append(finding("ERROR","YAML_PARSE_ERROR","<unknown>",str(e),rel));continue
        if not isinstance(d,dict):
            fs.append(finding("ERROR","RECORD_NOT_OBJECT","<unknown>","Top-level YAML must be an object.",rel));continue
        d["_path"]=rel;recs.append(d)
    by={}
    for r in recs:
        path=r["_path"]; rid=str(r.get("recordId","")).strip() or "<missing>"
        rt=r.get("recordType"); px=TYPE2PREFIX.get(rt)
        if not px:
            fs.append(finding("ERROR","UNKNOWN_RECORD_TYPE",rid,f"Unknown recordType {rt!r}.",path));continue
        m=ID_RE.fullmatch(rid)
        if not m or m.group(1)!=px: fs.append(finding("ERROR","INVALID_ID_PATTERN",rid,f"Expected {px}-YYYY-NNN.",path))
        if rid in by: fs.append(finding("ERROR","DUPLICATE_RECORD_ID",rid,f"Also used by {by[rid]['_path']}.",path))
        else: by[rid]=r
        if r.get("status") not in CFG[px]["statuses"]: fs.append(finding("ERROR","UNKNOWN_STATUS",rid,f"Invalid status {r.get('status')!r}.",path))
        if r.get("confidentiality") not in CONF: fs.append(finding("ERROR","UNKNOWN_CONFIDENTIALITY",rid,f"Invalid confidentiality {r.get('confidentiality')!r}.",path))
        lvl=(r.get("materiality") or {}).get("level")
        if rt!="PROFESSIONAL_DISSENT" and lvl not in MAT: fs.append(finding("ERROR","UNKNOWN_MATERIALITY",rid,f"Invalid materiality {lvl!r}.",path))
        for fld in ("title","createdAt","updatedAt"):
            if not nonempty(r.get(fld)): fs.append(finding("ERROR","REQUIRED_FIELD_MISSING",rid,f"{fld} is required.",path))
        for fld in ("createdAt","updatedAt"):
            if date(r.get(fld)) is None: fs.append(finding("ERROR","INVALID_DATE",rid,f"{fld} must be YYYY-MM-DD.",path))
        if rt=="DECISION":
            if not nonempty((r.get("decisionOwner") or {}).get("role")): fs.append(finding("ERROR","DECISION_OWNER_REQUIRED",rid,"decisionOwner.role is required.",path))
            if not nonempty(r.get("decision")): fs.append(finding("ERROR","DECISION_TEXT_REQUIRED",rid,"decision is required.",path))
            sched=date((r.get("review") or {}).get("scheduledDate"))
            if sched and sched<=today and r.get("status") not in {"REVIEW_DUE","CLOSED","SUPERSEDED"}:
                fs.append(finding("WARNING","DECISION_REVIEW_DUE",rid,f"Review date {sched} reached.",path))
        elif rt in {"EXCEPTION","RISK_ACCEPTANCE"}:
            ref=(r.get("relatedDecisionOrEvent") or {}).get("ref")
            if not nonempty(ref): fs.append(finding("ERROR","RELATED_DECISION_REQUIRED",rid,"Non-primary record must reference a decision.",path))
            if rt=="EXCEPTION" and r.get("status") in {"APPROVED","ACTIVE","REVIEW_DUE"} and not nonempty((r.get("approvingAuthority") or {}).get("role")):
                fs.append(finding("ERROR","APPROVING_AUTHORITY_REQUIRED",rid,"Active/approved exception needs approvingAuthority.role.",path))
            if rt=="RISK_ACCEPTANCE" and r.get("status") in {"ACCEPTED","MITIGATING","MONITORING","REVIEW_DUE"}:
                if not nonempty((r.get("acceptedBy") or {}).get("role")): fs.append(finding("ERROR","ACCEPTING_AUTHORITY_REQUIRED",rid,"Accepted risk needs acceptedBy.role.",path))
                if not nonempty((r.get("monitoringOwner") or {}).get("role")): fs.append(finding("ERROR","MONITORING_OWNER_REQUIRED",rid,"Accepted risk needs monitoringOwner.role.",path))
            exp=date(r.get("expiryDate"))
            terminal={"EXCEPTION":{"EXPIRED","REVOKED","INCORPORATED_INTO_STANDARD"},"RISK_ACCEPTANCE":{"CLOSED","REVOKED"}}[rt]
            if exp and exp<today and r.get("status") not in terminal:
                fs.append(finding("WARNING","EXCEPTION_EXPIRED" if rt=="EXCEPTION" else "RISK_REVIEW_DUE",rid,f"expiryDate {exp} passed.",path))
        elif rt=="PROFESSIONAL_DISSENT":
            ref=(r.get("relatedDecision") or {}).get("ref")
            if not nonempty(ref): fs.append(finding("ERROR","RELATED_DECISION_REQUIRED",rid,"Dissent must reference a decision.",path))
            ack=r.get("acknowledgedByDecisionOwner") or {}
            if r.get("status") in {"ACKNOWLEDGED","RESOLVED_BY_DECISION"} and ack.get("acknowledged") is not True:
                fs.append(finding("ERROR","DISSENT_ACK_INCONSISTENT",rid,"Acknowledged/resolved dissent must set acknowledged=true.",path))
    for r in recs:
        rid=str(r.get("recordId","<missing>")); path=r["_path"]; rt=r.get("recordType"); refs=[]
        if rt in {"EXCEPTION","RISK_ACCEPTANCE"}: refs=[((r.get("relatedDecisionOrEvent") or {}).get("ref"),"DEC")]
        elif rt=="PROFESSIONAL_DISSENT": refs=[((r.get("relatedDecision") or {}).get("ref"),"DEC")]
        elif rt=="DECISION":
            refs += [(x,"EXC") for x in (r.get("linkedExceptions") or [])]
            refs += [(x,"RSK") for x in (r.get("linkedRiskAcceptances") or [])]
            refs += [(x,"DSS") for x in (r.get("linkedDissent") or [])]
        for ref,expected in refs:
            if not nonempty(ref):continue
            target=by.get(str(ref))
            if not target: fs.append(finding("ERROR","MISSING_RELATIONSHIP",rid,f"{ref} does not resolve.",path));continue
            actual=TYPE2PREFIX.get(target.get("recordType"))
            if actual!=expected: fs.append(finding("ERROR","RELATIONSHIP_TYPE_MISMATCH",rid,f"{ref} expected {expected}, found {actual}.",path))
    return recs,sorted(fs,key=lambda f:(f["severity"]!="ERROR",f["recordId"],f["code"]))

def next_id(px,year):
    mx=0
    for p in files():
        try:r=load(p) or {}
        except Exception:continue
        m=ID_RE.fullmatch(str(r.get("recordId","")))
        if m and m.group(1)==px and int(m.group(2))==year: mx=max(mx,int(m.group(3)))
    return f"{px}-{year}-{mx+1:03d}"

def snapshot(today=None):
    today=today or dt.date.today(); recs,fs=validate(today)
    if any(f["severity"]=="ERROR" for f in fs): return None,fs
    byid={r["recordId"]:r for r in recs if "recordId" in r}
    def brief(r):
        return {"recordId":r.get("recordId"),"recordType":r.get("recordType"),"title":r.get("title"),"status":r.get("status"),"materiality":(r.get("materiality") or {}).get("level"),"updatedAt":str(r.get("updatedAt")) if r.get("updatedAt") is not None else None,"confidentiality":r.get("confidentiality"),"path":r.get("_path")}
    dec=[r for r in recs if r.get("recordType")=="DECISION"]; exc=[r for r in recs if r.get("recordType")=="EXCEPTION"]; risk=[r for r in recs if r.get("recordType")=="RISK_ACCEPTANCE"]; dss=[r for r in recs if r.get("recordType")=="PROFESSIONAL_DISSENT"]
    due={f["recordId"] for f in fs if f["code"] in {"DECISION_REVIEW_DUE","EXCEPTION_EXPIRED","RISK_REVIEW_DUE"}}
    material_dss=[]
    for d in dss:
        ref=(d.get("relatedDecision") or {}).get("ref"); parent=byid.get(ref,{})
        if d.get("status") in {"RECORDED","ACKNOWLEDGED"} and (parent.get("materiality") or {}).get("level") in {"M2","M3","M4"}: material_dss.append(brief(d))
    missing_out=[]
    for d in dec:
        o=d.get("outcome") or {}
        if d.get("status") in {"DECIDED","EXECUTING","REVIEW_DUE","CLOSED"} and not nonempty(o.get("observedOutcome")) and not (o.get("evidenceRefs") or []): missing_out.append(brief(d))
    return {"schemaVersion":"1.0","kind":"ExecutiveDecisionControlCenterReadModel","generatedAt":dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat(),"asOfDate":today.isoformat(),"source":{"system":"ADM-ORG-DER-001","authoritative":False,"rule":"Projection only; source records remain authoritative."},"metrics":{"totalRecords":len(recs),"decisions":len(dec),"activeExceptions":sum(r.get("status") in {"APPROVED","ACTIVE","REVIEW_DUE"} for r in exc),"acceptedRisks":sum(r.get("status") in {"ACCEPTED","MITIGATING","MONITORING","REVIEW_DUE"} for r in risk),"openDissent":sum(r.get("status") in {"RECORDED","ACKNOWLEDGED"} for r in dss),"reviewDue":len(due),"validationWarnings":sum(f["severity"]=="WARNING" for f in fs)},"views":{"openDecisionsByMateriality":[brief(r) for r in dec if r.get("status") not in {"CLOSED","SUPERSEDED"}],"decisionsAwaitingInput":[brief(r) for r in dec if r.get("status")=="PENDING_INPUT"],"reviewDue":[brief(r) for r in recs if r.get("recordId") in due],"activeExceptions":[brief(r) for r in exc if r.get("status") in {"APPROVED","ACTIVE","REVIEW_DUE"}],"acceptedRisksAwaitingReview":[brief(r) for r in risk if r.get("status") in {"ACCEPTED","MITIGATING","MONITORING","REVIEW_DUE"}],"materialDissentLinkedToActiveDecisions":material_dss,"decisionsWithoutExecutionOutcome":missing_out,"validationFindings":fs}},fs

def parse_day(v): return dt.date.fromisoformat(v) if v else None

def main():
    p=argparse.ArgumentParser(description="Operate ADM-ORG-DER-001 records."); s=p.add_subparsers(dest="cmd",required=True)
    v=s.add_parser("validate");v.add_argument("--today");v.add_argument("--strict",action="store_true")
    n=s.add_parser("next-id");n.add_argument("type",choices=sorted(CFG));n.add_argument("--year",type=int)
    q=s.add_parser("snapshot");q.add_argument("--today");q.add_argument("--output")
    a=p.parse_args()
    if a.cmd=="validate":
        recs,fs=validate(parse_day(a.today))
        for f in fs: print(f'{f["severity"]}: {f["code"]}: {f["recordId"]}: {f["message"]} [{f["path"]}]')
        e=sum(f["severity"]=="ERROR" for f in fs);w=sum(f["severity"]=="WARNING" for f in fs)
        print(f"Validated {len(recs)} actual record(s): {e} error(s), {w} warning(s).")
        return 1 if e or (a.strict and w) else 0
    if a.cmd=="next-id": print(next_id(a.type,a.year or dt.date.today().year));return 0
    data,fs=snapshot(parse_day(a.today))
    if data is None: print("Snapshot not produced because validation failed.",file=sys.stderr);return 1
    payload=json.dumps(data,ensure_ascii=False,indent=2)+"\n"
    if a.output:
        out=(ROOT/a.output).resolve() if not Path(a.output).is_absolute() else Path(a.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(payload,encoding="utf-8");print(out)
    else: print(payload,end="")
    return 0
if __name__=="__main__": raise SystemExit(main())
