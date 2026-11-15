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

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others: 10 a minute is the same as one requst every 6 seconds, this is a reasonable limit for a writer going back and forth with the model to change specific things, typing a request after just sending one every 6 seconds is difficult for a human, first they user has to type the prompt, but usually the user reads the response of the prvious prompt before sending the new one. If the human user was making incrememntal small changes, 10 a minute is a reasonable limit allowing quick changes while limiting potnential scripts attempting many requests in a short timeframe. 200 a day restricts slower automted submissions.**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as: per creator_id, if none available, fallback to ip address.** <!-- per address, or per creator_id? They fail differently — one script can look like a thousand callers, and one household can look like one. -->

**The run of status codes when I pushed past it: The last 5 of the 15 requests were rejected with a 429 code.**

<!-- python run_attacks.py --flood 15 -->

```
============================================================
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
============================================================

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->
     | ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `e09a70e8-9e5c-48ee-906c-74f00a19d448` | human| 0.310 |BROKE|
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `9476eaa3-161d-43c1-8a6b-2485f68d4dc0` | unsure | 0.500 |BROKE|
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `ece0d621-d95b-4f68-9409-39cdb2a1f9cb` | unsure | 0.478 |BROKE|
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `9052dca6-ca54-4e87-8d7f-e07ddbeb4ed8` | unsure | 0.526 |BROKE|
| EV05 | evasion | both signals: heavy human editing pass | 200 | `b9e747c5-40eb-4142-8974-9cd659288c25` | human | 0.263 |BROKE|
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `bc697553-d554-40d5-8c52-355f78c7e394` | unsure | 0.395 |BROKE|
| EV07 | evasion | signal two: padding with punctuation | 200 | `586a2efe-e2d3-4a6c-bba3-00475e85a9fa` | unsure | 0.543 |BROKE|
| EV08 | evasion | signal one: text below the token window | 200 | `84e57759-76ed-45f5-9b66-f09dfec2aa34` | unsure | 0.373 |BROKE|
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `22e101b5-7f5c-4fab-8d97-2d898ec742aa` | unsure | 0.493 |BROKE|
| EV10 | evasion | signal two: repeated stanza structure | 200 | `5cb931fb-e469-4354-9b1c-54b1d0d629e5` | ai | 0.863 |HELD|
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `fbd5ed0b-528b-4a59-bcb6-4965187c3a2f` | unsure | 0.528 |HELD|
| FP02 | false_positive | human writing in a formal register | 200 | `c3d7fbc9-fc4c-44d4-a2f6-96b6f90b6338` | unsure | 0.646 |HELD|
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `fcbf731c-44f1-4ab9-a56c-bf8bb83430c3` | ai | 0.657 |BROKE|
| FP04 | false_positive | a student essay written to a rubric | 200 | `0adfff32-655b-497c-abfb-72f306873aa2` | unsure | 0.603 |HELD|
| FP05 | false_positive | technical documentation written by a person | 200 | `9b7e2492-27e3-4389-a6c7-04916852d9d6` | ai | 0.712 |BROKE|
| FP06 | false_positive | a person imitating a formal template | 200 | `a6028ceb-8c7a-4505-9bc6-7dafcd1b1baa` | unsure | 0.500 |HELD|
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `f441c7be-683e-4b57-a577-ff782f323943` | ai | 0.671 |BROKE|
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |BROKE|
| PI01 | prompt_injection | instruction to ignore the check | 200 | `3118d5df-ad6f-4a7f-8306-18e3975cd87f` | human | 0.325 |BROKE|
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `5c72dc28-f9c7-4ac0-a3c7-0cb00bb0fc68` | human | 0.173 |HELD|
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `21452b39-fd0c-486d-a247-b8a6314c9ff1` | unsure | 0.475 |HELD|
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `0b6a37ac-89cf-4121-9530-8d32c8379a0a` | unsure | 0.408 |HELD|
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `ad6ed416-cf49-4f0f-8555-3cd83986bd8b` | unsure | 0.412 |HELD|
| PI06 | prompt_injection | instruction plus real human text | 200 | `8beebf31-4556-49d4-bb2b-79ea6df12bcf` | unsure | 0.502 |HELD|
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |HELD|
| MF02 | malformed | text is a single character | 400 | `—` | — | — |HELD|
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  HELD
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |HELD|
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |HELD|
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |HELD|
| MF07 | malformed | text is right-to-left script | 200 | `a44a842c-f4fa-4d2a-9d6f-454d96533034` | ai | 0.703 |BROKE|
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |HELD|
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |HELD|
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |HELD|
| RQ03 | malformed | text is a number | 400 | `—` | — | — |HELD|
| RQ04 | malformed | text is a list | 400 | `—` | — | — |HELD|
| RQ05 | malformed | text is null | 400 | `—` | — | — |HELD|
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |HELD|
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |HELD|
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |HELD|
| RQ09 | malformed | body is empty | 400 | `—` | — | — |HELD|
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |HELD|
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |HELD|
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |HELD|
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |HELD|
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |HELD|
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |HELD|



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "3118d5df-ad6f-4a7f-8306-18e3975cd87f", "creator_id": "attacker_PI01", "guess": "human", "model_score": 0.4625, "style_score": 0.18836790191743583, "combined_score": 0.3254339509587179, "label": "This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.", "status": "decided"}
{"timestamp": "2026-11-15T18:24:00+00:00", "content_id": "a44a842c-f4fa-4d2a-9d6f-454d96533034", "creator_id": "attacker_MF07", "guess": "ai", "model_score": 0.9064, "style_score": 0.5, "combined_score": 0.7032, "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "creator_id": "attacker_FP08", "event": "rejected", "status": "rejected", "reason": "text_too_short_or_invalid"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "f441c7be-683e-4b57-a577-ff782f323943", "creator_id": "attacker_FP07", "guess": "ai", "model_score": 0.8816, "style_score": 0.46015394727152886, "combined_score": 0.6708769736357645, "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "9b7e2492-27e3-4389-a6c7-04916852d9d6", "creator_id": "attacker_FP05", "guess": "ai", "model_score": 0.8005, "style_score": 0.6226436597131433, "combined_score": 0.7115718298565716, "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "fcbf731c-44f1-4ab9-a56c-bf8bb83430c3", "creator_id": "attacker_FP03", "guess": "ai", "model_score": 0.8051, "style_score": 0.50914375565228, "combined_score": 0.6571218778261401, "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "9476eaa3-161d-43c1-8a6b-2485f68d4dc0", "creator_id": "attacker_EV02", "guess": "unsure", "model_score": 0.5943, "style_score": 0.07314560439560447, "combined_score": 0.5, "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "9052dca6-ca54-4e87-8d7f-e07ddbeb4ed8", "creator_id": "attacker_EV04", "guess": "unsure", "model_score": 0.6114, "style_score": 0.44047989395068177, "combined_score": 0.525939946975341, "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "22e101b5-7f5c-4fab-8d97-2d898ec742aa", "creator_id": "attacker_EV09", "guess": "unsure", "model_score": 0.7042, "style_score": 0.28166172011026624, "combined_score": 0.49293086005513315, "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.", "status": "decided"}
{"timestamp": "2026-11-15T18:23:59+00:00", "content_id": "586a2efe-e2d3-4a6c-bba3-00475e85a9fa", "creator_id": "attacker_EV07", "guess": "unsure", "model_score": 0.5862, "style_score": 0.5, "combined_score": 0.5431, "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.", "status": "decided"}


```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it: FP05, a technical documentation written by a person, was marked human by the system. A technical documentation usually follow format, specific and repeitive vocabulary tailored to the subject. On top of that, technical documents usually take a lot of time to write and are high effort as they are specific and people rely on said document for understanding.  Given that usually a writier must follow conventional writing practices for the document, I'd least like to explain to the writer of a high effort document that there were flagged for essentially doing the right thing.



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
|1. False positives|≤5%|4/20 (20%)|4/20 (20%)|4/20 (20%)|MISSED|
|2. Score separation|≥0.30|-0.084|-0.084|-0.084|MISSED|
|3. Label coverage|	3/3|3/3|3/3|3/3|MET|
|4. Appeals recorded|100%|3/3|3/3|3/3|MET|
|5. Malformed requests|10/10|10/10|10/10|10/10|MET|



**Real output from one trial**, pasted as text, naming the file and function
that produced it: Source: results/run_2026-11-15_1820_before.md / run_eval.py::main

```json
### my own writing — Trial 1
Source: results/run_2026-11-15_1820_before.md / run_eval.py::main
```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6903962747690247,
    "model_score": 0.6051,
    "style_score": 0.7756925495380493,
    "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.",
    "sent": "Greek city states were all part of Greece and rule themselves, because"
  }
]
```

### published human writing — Trial 1
Source: results/run_2026-11-15_1820_before.md / run_eval.py::main
```json
[
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.6698351321855764,
    "model_score": 0.6864,
    "style_score": 0.653270264371153,
    "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.",
    "sent": "I could have shown the infl ow of energy coming from a cloud, but inst"
  }
]
```

### AI writing for score separation — Trial 1
Source: results/run_2026-11-15_1820_before.md / run_eval.py::main
```json
[
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5695519355779541,
    "model_score": 0.6435,
    "style_score": 0.4956038711559083,
    "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
    "sent": "Effective time management is an important skill for students who want "
  }
]
```

### label coverage — Trial 1
Source: results/run_2026-11-15_1820_before.md / run_eval.py::main
```json
[
  {
    "status": 200,
    "guess": "human",
    "confidence": 0.30977815838547235,
    "model_score": 0.1635,
    "style_score": 0.4560563167709447,
    "label": "This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.",
    "sent": "The importance of effective communication in the workplace cannot be o"
  },
  {
    "status": 200,
    "guess": "unsure",
    "confidence": 0.5280441578766563,
    "model_score": 0.6175,
    "style_score": 0.43858831575331253,
    "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
    "sent": "We got to the campsite about four. The pitch was fine, a bit sloped, b"
  },
  {
    "status": 200,
    "guess": "ai",
    "confidence": 0.7115718298565716,
    "model_score": 0.8005,
    "style_score": 0.6226436597131433,
    "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.",
    "sent": "To configure the service, edit the settings file in the installation d"
  }
]
```

### bad input — Trial 1
Source: results/run_2026-11-15_1820_before.md / run_eval.py::main
```json
[
  {
    "status": 400,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "(empty text)"
  },
  {
    "status": 413,
    "guess": null,
    "confidence": null,
    "model_score": null,
    "style_score": null,
    "label": null,
    "sent": "word word word word word word word word word word word word word word "
  }
]
```


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


Criterion 1 - MISSED: False-positive rate
The system falsely classified 4 of 20 verified human passages as AI-generated (20%), exceeding my maximum acceptable rate of 5%. This happened identically across all three trials. The failures occurred in the detection signals and combining rule. In my writing #9, the stylometric score of 0.7757 raised the combined score to 0.6904 despite the lower model score of 0.6051. In writing #10, both signals were relatively high (model 0.7268, style 0.6513), producing a combined score of 0.6891. This demonstrates that the stylometric heuristics can mistake features of authentic human writing for AI-generated patterns. The combining rule also allows moderately high scores from both signals to produce a false AI classification.

Criterion 2 - MISSED: Score separation
The average combined score for the 20 human passages was 0.5962, while the average for the 10 AI generated passages was 0.5122. The resulting separation was -0.0840, substantially below my required positive separation of 0.30. The failure is in the detection signals and their combination, rather than merely the final label mapping. The signals failed to distinguish these groups in the intended direction, and the combining rule did not correct that overlap. All ten AI generated samples were classified as unsure. Changing only the AI classification threshold would not resolve the underlying problem of AI generated writing receiving lower average scores than human writing.

| Attack | Stage | Mechanism |
|---|---|---|
| EV03 | Signal two and combining rule | Adding a conversational quotation produced a relatively low stylometric score of 0.2889 despite a model score of 0.6662. The combining rule averaged both signals, producing 0.4776 (`unsure`). |
| EV04 | Signal one and combining rule | Unusual vocabulary targeted model perplexity. The resulting model score was 0.6114 and the style score was 0.4405, yielding 0.5259 (`unsure`). This demonstrates insufficient detection of the modified text, although a control sample would be needed to establish the vocabulary substitutions' precise effect. |
| EV05 | Both detection signals | Heavy human editing produced low scores from both the model (0.3212) and stylometry (0.2051). Their average of 0.2631 incorrectly classified the AI-origin text as human. Neither signal maintained sufficient discrimination after substantial editing. |
| EV06 | Signal two and combining rule | Combining an unusually long sentence with a very short sentence produced a low style score of 0.2179 versus a model score of 0.5727. The average of 0.3953 resulted in `unsure`, demonstrating sensitivity to manipulated sentence-length patterns. |
| EV07 | Signal two and combining rule | Punctuation padding produced a neutral style score of exactly 0.5000. Because the input is structured as a long semicolon-separated sentence, this is consistent with the stylometric fallback for insufficient sentence count. The model score of 0.5862 and neutral style score averaged to 0.5431 (`unsure`). |
| EV08 | Signal one and signal two | The ten-word submission passed the route's minimum-length validation but fell below stylometry's 20-word minimum, causing the neutral fallback of 0.5000. The model scored the short text at only 0.2452. Their average of 0.3726 avoided an AI classification. |
| EV09 | Signal two and combining rule | Adding a conversational human introduction to AI-generated writing produced a model score of 0.7042 but a much lower stylometric score of 0.2817. Their difference of approximately 0.4225 did not trigger the disagreement override. The normal average produced 0.4929 (`unsure`), masking the higher model signal. |

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
