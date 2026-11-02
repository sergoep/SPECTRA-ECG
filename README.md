# SPECTRA-ECG: Spectral Routing for Budget-Aware Multimodal ECG Review

A non-diagnostic research prototype for deciding **where expensive
multimodal AI attention should be spent** in long ECG streams.

## Core pipeline

`long ECG → frozen spectral scout → Top-K 5-s lead-II windows → ECG image panels → Meta Muse Spark 1.3 → structured review evidence`

The spectral router is frozen from the independently archived V5.2
package (Zenodo DOI `10.5281/zenodo.23866944`). The hackathon
contribution is the multimodal Meta integration, blind route locking,
structured evidence layer, API workload instrumentation, and
truth-sealed end-to-end evaluation.

## Locked hackathon result

The Meta demo subset was selected by SHA-256 ordering of record IDs
before endpoint truth was opened: records I55, I42, I58 and I37; 1,440
windows; 4 patients; 2,045 endpoint events.

  --------------------------------------------------------------------------------
  Route        Windows to      Scout   End-to-end    Logical    Logical    Logical
                     Muse   coverage       recall API panels     tokens route cost
  ------------ ---------- ---------- ------------ ---------- ---------- ----------
  FULL              1,440    100.00%       99.90%        180    955,896   \$1.6612
                   (100%)                                               

  SPECTRA-10    144 (10%)     11.74%       11.69%         18     95,357   \$0.1651

  SPECTRA-20    288 (20%)     22.20%       22.10%         36    192,031   \$0.3359
  --------------------------------------------------------------------------------

At the 10% route, the fair per-route workload comparison reduces logical
token use by **90.02%** and logical route cost by **90.06%**, while
retaining **11.70%** of FULL end-to-end endpoint recall. At 20%, token
use falls **79.91%**, logical route cost **79.78%**, and retained FULL
end-to-end recall is **22.12%**.

Muse was not used as a diagnostic system. Within the routed sets it
removed 30/144 windows at 10% and 65/288 at 20%, while retaining
approximately **99.58%** and **99.56%**, respectively, of the endpoint
mass already captured by the spectral scout.

## Important accounting distinction

The notebook uses a local response cache. `FINAL_ROUTE_SUMMARY.csv`
reports the workload each route would require if executed independently,
which is the correct fair comparison between FULL, SPECTRA-10 and
SPECTRA-20. It is **not** the literal billed request count of this
particular cached execution.

The locked stage made **224 actual Meta requests** plus 10 local-cache
hits; the pilot made 2 actual requests. The measured pilot+locked API
cost reconstructed from unique response diagnostics is approximately
**\$2.0898**.

## Reproduce

1.  Open
    `notebooks/SPECTRA_ECG_META_FINAL_X10_MULTIMODAL_V1_3_META_RESPONSE_FIX.ipynb`
    in Google Colab.
2.  Add `MODEL_API_KEY` as a Colab secret.
3.  Keep `RUN_LOCKED=False` through the pilot.
4.  Inspect pilot JSON validity and projected spend.
5.  Set `RUN_LOCKED=True` only for the locked run.
6.  Ground truth is first read after `PRE_TRUTH_INFERENCE_SEAL.json` is
    created.
7.  Run `python src/verify_results.py` against the included result
    directory for an independent hash/metric check.

## Safety and scope

This is **review prioritization**, not diagnosis. The endpoint is the
project-specific review-relevant annotation endpoint inherited from the
frozen experiment. No claim is made that Walsh is intrinsically superior
to Haar or Fourier; V5.2 in fact found higher pooled event-weighted
coverage for HaarDWT than Walsh12 at the tested budgets.

## Hackathon fit

Recommended entry: **Indie Developer Track / Push the Frontier**. Meta
describes the Indie track as for individual builders and students and
the Push the Frontier theme as using Meta models to accelerate
scientific experiments or understand/control physical systems.

## Files

-   `notebooks/` --- final locked Colab experiment.
-   `results/core/` --- primary locked results and seals.
-   `results/figures/` --- submission-ready figures.
-   `results/audit/` --- independent X10 audit, cache-aware API
    accounting, heterogeneity and exploratory permutation check.
-   `docs/` --- submission copy, demo script, one-page technical brief,
    and audit report.
-   `artifacts/` --- untouched original locked results ZIP.
