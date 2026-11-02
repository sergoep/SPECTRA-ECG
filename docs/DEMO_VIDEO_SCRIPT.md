# 2--3 Minute Demo Video Script

## 0:00--0:20 --- The problem

Show a long ECG trace and say:

"Long recordings contain thousands of short windows. Sending every
window to a multimodal model is expensive and unnecessary. SPECTRA-ECG
asks a simpler question first: where should AI attention be spent?"

## 0:20--0:45 --- Architecture

Show the pipeline diagram/text:

`ECG → frozen spectral scout → Top-K windows → waveform panels → Muse Spark 1.3 → structured evidence`

Explain that the scout is deterministic and frozen. Muse never receives
the hidden endpoint labels or scout score.

## 0:45--1:15 --- Working prototype

Open the Colab notebook. Show: - the exact lead-II panel; - the locked
routes FULL, 10%, 20%; - a Muse structured response containing
`window_id`, `review`, `priority`, `signal_quality`, `confidence`, and
`visual_evidence`.

State clearly: "This is review evidence, not a diagnosis."

## 1:15--1:50 --- Locked result

Show `fig_meta_cost_tradeoff.png` and the summary table.

Say:

"In the locked 1,440-window run, the 10% route sent 144 windows instead
of 1,440. The fair per-route token workload fell by about 90%, and route
cost fell by about 90%. It retained 11.70% of FULL end-to-end endpoint
recall. At 20%, token use fell about 80% while retained FULL recall was
22.12%."

Then add:

"Muse filtered the routed sets while preserving about 99.6% of the
endpoint mass already captured by the spectral scout."

## 1:50--2:15 --- Integrity

Show `PRE_TRUTH_INFERENCE_SEAL.json` and FINAL-X10.

"The routes and Muse outputs were frozen before ground truth was opened.
The decision file was SHA-256 sealed, and every final integrity check
passed."

## 2:15--2:40 --- Why Meta

"Spectral routing provides cheap deterministic attention control. Muse
Spark adds native visual reasoning and structured human-readable
evidence. Together they turn a long signal into a budget-controlled
review workflow."

## 2:40--2:55 --- Limitation / close

"This is a non-diagnostic research prototype. The demo subset is small,
and the scientific benchmark does not claim Walsh is universally best.
The contribution is an auditable way to allocate multimodal AI compute
to real signals."

End card: **SPECTRA-ECG --- Spend AI attention where the signal says it
matters.**
