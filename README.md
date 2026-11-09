# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->
1) Recieve and validate the submission (app.py::submit)
2) Generate a content identifier
3) Analayze the writing (detector.py anmd stylometry.py)
4) Combine the signals (scoring.py::combine_signals)
5) Generate a classification (scoring.py::score_to_label)
6) Record the decision (audit.py:log_decision)
7) Return the response (app.py::submit)


---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures: Measures the perplexity of each submitted writing, how predictable the next sequence of text is to an AI.**

**Why that might differ between human and AI writing: Ai is good at prediciting AI, since genereated text is based off leared probability distributions, humans on the other hand are more likely to have unusual phrasing, unexepected word choices, etc.**

**What it can't see: It cannot see who wrote the text and whether they truly are a human or an AI.**

### Signal two — the style signal

**What it measures: The statistical and stylistic characteristics of a submitted wirting.**

**Why that might differ between human and AI writing: AI writing usually contains consistent sentence structure, vocabulary patterns and punctuation. While human writing usually contains more irregularities, stylistic variation and different phrasing**

**What it can't see: Cannot see if specific writing patterns were made by an AI or a human.**

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule: If the two signals substantially disagree, the system returns an uncertain score rather than producing a potentially misleading classification.**

**The numbers: High-confidence human: Score ≤ 0.35, Unsure: 0.35 < Score < 0.65, High-confidence AI: Score ≥ 0.65**

**Where it lives: scoring.py::combine_signals** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
During testing, one submission produced a model score of 0.7424 and a stylometric score of 0.4667. The signals differed by approximately 0.276, indicating some disagreement but not exceeding my disagreement threshold of 0.50. So the system applied its normal weighted average, producing  an unsure classification. If the difference had reached 0.50 or greater, my combining rule would instead have returned a neutral score of 0.50.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human |0.00–0.35|This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.|
| unsure |>0.35 & <0.65|We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.|
| high-confidence AI |0.65-1.00|This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.|


**Why I worded the "unsure" one this way:**
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->
I wanted to communicate uncertainty without implying that the writer had done something wrong. Since both detection signals have limitations, an uncertain classification should not be treated as evidence of AI authorship.


---

## Sample Run

**A submission**

```bash
curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "Writing is an important part of human communication. People express their ideas in many different ways. Some writers prefer short sentences, while others use complicated structures. Every individual develops their own style through experience and practice.", "creator_id": "writer001"}'
```

```json
{
  "confidence": 0.6045600526200928,
  "content_id": "0b4fe800-a7e3-42ea-b96b-c7144b7f63d4",
  "guess": "unsure",
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "model_score": 0.7424,
  "style_score": 0.4667201052401857
}
```

**An appeal**

```bash
curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "0b4fe800-a7e3-42ea-b96b-c7144b7f63d4", "reasoning": "I wrote this myself and request human review."}'
```

```json
{
  "content_id": "0b4fe800-a7e3-42ea-b96b-c7144b7f63d4",
  "message": "Appeal recorded for human review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.6045600526200928,
      "content_id": "0b4fe800-a7e3-42ea-b96b-c7144b7f63d4",
      "creator_id": "writer001",
      "guess": "unsure",
      "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
      "model_score": 0.7424,
      "status": "decided",
      "style_score": 0.4667201052401857,
      "timestamp": "2026-11-09T08:00:01+00:00"
    },
    {
      "content_id": "0b4fe800-a7e3-42ea-b96b-c7144b7f63d4",
      "creator_id": "writer001",
      "event": "appeal",
      "reasoning": "I wrote this myself and request human review.",
      "status": "under_review",
      "timestamp": "2026-11-09T08:00:01+00:00"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:Help comparing different ways to combine the detection signals and implementing the backend functionality.*
- *What came back:Several scoring approaches, and explanations of their tradeoffs*
- *What I changed: I adapted the pipeline into my README, corrected the references to the scoring functions, and separated the submission workflow from the appeal process.*

**Moment 2**

- *What I asked for: Help understanding the project architecture, organizing the submission pipeline, and identifying how the different components interact.*
- *What came back:A  explanation of how requests travel through the API, detection signals, scoring system, classification, and audit logging.*
- *What I changed:I chose the disagreement-aware approach because conflicting signals shouldn't result in a confident label. I chose equal signal weights (0.50 each) and a provisional disagreement threshold of 0.50.*

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
