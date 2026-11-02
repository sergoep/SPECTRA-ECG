# Independent X10 Audit of the Locked Meta Package

## Verdict

**PASS with one accounting correction.**

All 243 files listed in the internal SHA-256 manifest match their
recorded sizes and hashes. The manifest intentionally cannot hash
itself; `SHA256_MANIFEST.csv` is the only unmanifested root file.

The four pre-truth seals independently recompute exactly: - decision
file:
`26a2d9b1aee97184d89c57d68afd0c5ffa2d88cfd7229b1b21f9db55d67048fc` -
API-call log:
`d1af779ad5965cd3d90433b7e259f8a6b54561eec5b67ab996516a5b263fac38` -
route membership:
`154feb49e01c97e03ae40dd9b9e299ceb7b84e68ea8802ce51744f0af374a25f` -
subset selection:
`70ba27ecd7f441d7de6084626fa7f1428f36f0b0233fb5e3f6ac72fde6b9b6c3`

All FINAL-X10 and post-seal truth-integrity checks are `True`.

## Independent metric recomputation

The four-record subset contains 2,045 endpoint events. Recomputed event
counts are: - FULL: 2,045 scout events; 2,043 in Muse-flagged windows. -
SPECTRA-10: 240 scout events; 239 in Muse-flagged windows. - SPECTRA-20:
454 scout events; 452 in Muse-flagged windows.

These reproduce the reported coverages and end-to-end recalls.

## Critical accounting correction

`FINAL_ROUTE_SUMMARY.csv` counts **logical route panels**, not literal
billed requests in this cached execution.

There are 234 logical panels: - 180 FULL - 18 SPECTRA-10 - 36 SPECTRA-20

But 10 locked-stage calls were local-cache hits. Therefore the locked
stage made **224 actual API requests**. The pilot made 2 actual
requests. The unique response diagnostics reconstruct: - locked actual
API cost: approximately **\$2.072865** - pilot + locked actual API cost:
approximately **\$2.089830**

The per-route values \$1.661178 / \$0.165129 / \$0.335856 remain useful
as **fair counterfactual independent-route workload estimates**, because
they price each logical panel using its observed token usage. They
should not be called the literal billed cost of this cached run.

## Model-response health

There are 226 unique actual response diagnostics. All completed with
non-null content; no refusal was recorded. The final model is standard
`muse-spark-1.3`, not Contributor mode.

## Heterogeneity warning

The subset has only four patients. Record I42 contributes 1,563 / 2,045
= **76.43%** of endpoint event mass. This prevents a strong
patient-population inference from the Meta subset.

An exploratory, post-hoc 100,000-repeat record-stratified equal-budget
random-allocation test gives upper-tail p-values around 0.009 for the
10% and 20% scout event counts. This is evidence against uniform
allocation on these fixed records, but it is **not** a preregistered
population-level test and should not be a headline hackathon claim.

## Final scientific status

-   Technical integrity: strong.
-   Compute/workload result: established for this locked run.
-   Muse as evidence generator: supported.
-   Muse as clinical classifier: not established.
-   Walsh superiority: not established.
-   Population-level generalization from the four Meta records: not
    established.
