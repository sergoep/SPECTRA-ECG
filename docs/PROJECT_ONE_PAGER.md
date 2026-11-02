# SPECTRA-ECG --- Technical One-Pager

## Objective

Reduce multimodal AI workload on long ECG streams without pretending
that a frontier model should inspect every short segment.

## System

A frozen 12-dimensional Walsh spectral router ranks non-overlapping
5-second windows. Recordwise Top-K windows are rendered as exact lead-II
ECG panels, eight windows per panel. Meta Muse Spark 1.3 receives the
image and window IDs and returns strict structured review evidence.

## Experimental firewall

The four Meta records were selected by SHA-256 ordering of record IDs.
Route membership was frozen before inference. The prompt contained no
endpoint labels, annotation symbols, event counts, outcomes or Walsh
scores. Blind Muse outputs were sealed before the truth table was read.

Decision SHA-256:
`26a2d9b1aee97184d89c57d68afd0c5ffa2d88cfd7229b1b21f9db55d67048fc`

## Locked subset

-   4 records / 4 patients
-   1,440 windows
-   2,045 endpoint events
-   records: I55, I42, I58, I37

## Results

10% route: - 144 windows - scout coverage 11.7359% - end-to-end recall
11.6870% - 95,357 logical route tokens - \$0.165129 logical route cost -
90.02% token reduction vs FULL - 90.06% route-cost reduction vs FULL -
99.58% of scout-captured event mass retained after Muse review flagging

20% route: - 288 windows - scout coverage 22.2005% - end-to-end recall
22.1027% - 192,031 logical route tokens - \$0.335856 logical route
cost - 79.91% token reduction vs FULL - 79.78% route-cost reduction vs
FULL - 99.56% of scout-captured event mass retained after Muse review
flagging

## Stress-test limitations

The Meta subset is intentionally small and is not a replacement for the
44-record/20-patient V5.2 benchmark. Event mass is highly heterogeneous:
record I42 contains 1,563 of the 2,045 subset events (76.43%). Therefore
the locked demo supports a systems-level workload result, not a
population-level clinical claim.

The frozen scientific V5.2 benchmark also found HaarDWT higher than
Walsh12 in pooled event-weighted coverage at all tested budgets.
SPECTRA-ECG therefore makes no Walsh-superiority claim.

## Novelty status

**New application / new in this framework.** The spectral mathematics is
not claimed as new here. The hackathon contribution is the auditable
composition of frozen spectral routing with multimodal Muse evidence
under explicit compute budgets and truth sealing.
