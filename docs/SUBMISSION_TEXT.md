# Meta Global AI Developer Hackathon --- Submission Draft

## Project name

**SPECTRA-ECG**

## Tagline

**Spend multimodal AI attention where the signal says it matters.**

## Recommended track and theme

**Indie Developer Track --- Push the Frontier**

## Problem

Long physiological recordings contain far more data than a multimodal
model should process indiscriminately. Sending every five-second ECG
window to a frontier model wastes tokens, latency and cost, while a
purely lightweight router cannot provide the visual, human-readable
evidence that a reviewer wants.

## Solution

SPECTRA-ECG separates the problem into two layers. A deterministic
frozen spectral scout ranks ECG windows cheaply. Only the highest-ranked
windows are rendered as lead-II waveform panels and sent to **Meta Muse
Spark 1.3**, which returns a strict structured review-evidence object
for every window.

The model never receives the hidden endpoint labels, WFDB symbols, event
counts, patient outcomes or Walsh scores.

## What I built during the hackathon

The underlying spectral scout and its V5.2 scientific validation predate
the hackathon and are independently archived at Zenodo DOI
`10.5281/zenodo.23866944`.

During the hackathon I built: - the end-to-end multimodal ECG-to-Muse
pipeline; - visual batching of 5-second lead-II windows; - strict
JSON-schema review evidence from Muse Spark 1.3; - frozen FULL / 10% /
20% routing experiments; - a truth-sealed protocol in which model
outputs are SHA-256 fixed before labels are opened; - token, latency and
cost instrumentation; - an adversarial FINAL-X10 reproducibility audit.

## Locked result

On a pre-locked four-record, 1,440-window demonstration subset: - FULL
sent 1,440 windows to Muse; - SPECTRA-10 sent 144; - SPECTRA-20 sent
288.

SPECTRA-10 reduced the fair per-route token workload by **90.02%** and
estimated route cost by **90.06%**, while retaining **11.70%** of FULL
end-to-end endpoint recall. SPECTRA-20 reduced tokens by **79.91%** and
route cost by **79.78%**, while retaining **22.12%** of FULL end-to-end
endpoint recall.

Muse acted as a structured multimodal evidence layer rather than a
clinical classifier. At the 10% and 20% routes, it retained
approximately **99.6%** of the endpoint mass already captured by the
spectral scout while producing review-priority, signal-quality,
confidence and visual-evidence fields.

## Why Meta is essential

The spectral router answers **where should expensive attention go?**
Muse Spark answers **what visible evidence is present in the selected
waveform?** The product value comes from composing cheap deterministic
routing with native multimodal reasoning and structured output.

## Responsible scope

SPECTRA-ECG is not a diagnostic device and does not claim clinical
validation. It is a research prototype for budget-aware review
prioritization. The project explicitly reports negative and limiting
results, including that the four-record demo subset shows only moderate
spectral enrichment and that the scientific V5.2 benchmark did not
establish Walsh superiority over HaarDWT.

## Reproducibility

The locked decision file SHA-256 is:
`26a2d9b1aee97184d89c57d68afd0c5ffa2d88cfd7229b1b21f9db55d67048fc`

The uploaded locked-results ZIP SHA-256 is:
`8c30aa6ad6bf326b6d2aff6ee7ccc9be9fe4877eb150100d494d5858875595f4`

Frozen scientific archive: Zenodo DOI `10.5281/zenodo.23866944`
