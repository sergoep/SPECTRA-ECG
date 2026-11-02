#!/usr/bin/env python3
from pathlib import Path
import pandas as pd, json, hashlib, sys

ROOT=Path(__file__).resolve().parents[1]
R=ROOT/"results"/"core"

def sha(p):
    h=hashlib.sha256()
    with open(p,"rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()

seal=json.load(open(R/"PRE_TRUTH_INFERENCE_SEAL.json"))
assert sha(R/"LOCKED_META_DECISIONS_BLIND.csv")==seal["decisions_sha256"]
assert sha(R/"LOCKED_API_CALLS.csv")==seal["api_calls_sha256"]

routes=pd.read_csv(R/"LOCKED_ROUTE_MEMBERSHIP.csv")
route_hash=hashlib.sha256(
    routes.sort_values(["route","window_id"]).to_csv(index=False).encode()
).hexdigest()
assert route_hash==seal["route_membership_sha256"]

ev=pd.read_csv(ROOT/"artifacts"/"SPECTRA_ECG_META_FINAL_X10_MULTIMODAL_RESULTS.zip",
               compression="zip") if False else None

summary=pd.read_csv(R/"FINAL_ROUTE_SUMMARY.csv")
expected={"FULL_META":(1440,1.0),
          "SPECTRA_10_META":(144,0.11735941320293398),
          "SPECTRA_20_META":(288,0.22200488997555012)}
for route,(n,cov) in expected.items():
    row=summary.loc[summary.route.eq(route)].iloc[0]
    assert int(row.windows_sent_to_meta)==n
    assert abs(float(row.scout_endpoint_coverage)-cov)<1e-12

x10=pd.read_csv(R/"FINAL_X10_AUDIT.csv")
assert x10.passed.all()

print("PASS: seals, route summary, and FINAL-X10 verified.")
print("Decision SHA-256:",seal["decisions_sha256"])
