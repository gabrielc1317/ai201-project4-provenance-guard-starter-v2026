# Attack run — after

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-15 19:06
- Auto-marked BROKE (5xx, crash, no response): **0**
- Left for you to judge: **56**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `55b3492f-d8d8-4a85-8fe5-1a96f9b0f4f7` | human | 0.310 |  |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `842d0e13-287f-4aa7-8e95-e6c7b09a0cba` | unsure | 0.500 |  |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `65f438be-3fcf-4cc2-a6c3-84fa5ed1ed22` | unsure | 0.478 |  |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `76dadab1-1d10-48ae-aae4-604908eead98` | unsure | 0.526 |  |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `e154ec7a-560b-4c03-8205-181915e0cabb` | human | 0.263 |  |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `cb3cfded-ebd8-4da1-b02f-0c883139a26b` | unsure | 0.395 |  |
| EV07 | evasion | signal two: padding with punctuation | 200 | `d1a39e14-ea13-490d-bd58-ec42f17e7b7b` | unsure | 0.543 |  |
| EV08 | evasion | signal one: text below the token window | 200 | `6f42dfd2-3e9d-4cfc-9802-cfaceec754e7` | unsure | 0.373 |  |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `6f26339b-50e3-49ef-814a-c21e36311ee4` | unsure | 0.493 |  |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `d4219572-e1e3-4d1c-b62e-573cd313729a` | ai | 0.863 |  |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `ddfdc476-ffd1-4f7b-a212-5de66ec558f2` | unsure | 0.528 |  |
| FP02 | false_positive | human writing in a formal register | 200 | `79350416-3802-4340-aa9c-4b497ae82941` | unsure | 0.646 |  |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `8f98eafc-c18c-4066-9bac-0c926835bcf1` | unsure | 0.657 |  |
| FP04 | false_positive | a student essay written to a rubric | 200 | `3fe86e78-f7b5-418d-8a7a-4b05b06fd706` | unsure | 0.603 |  |
| FP05 | false_positive | technical documentation written by a person | 200 | `616ed947-b754-48db-8f7a-fbcaf1eeb090` | unsure | 0.712 |  |
| FP06 | false_positive | a person imitating a formal template | 200 | `e88aaee9-ca20-46f3-9ebe-6e3a2289239f` | unsure | 0.500 |  |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `a12f0ca0-0a42-4161-99bc-b35c979fac2f` | unsure | 0.671 |  |
| FP08 | false_positive | very short genuine human submission | 400 | `—` | — | — |  |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `7bc90852-4c6d-4900-a8cb-aa52f000b4e0` | human | 0.325 |  |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `9aceac4e-0be5-4f07-b6d5-13b26efc68f7` | human | 0.173 |  |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `190cff42-1e4f-4f7e-b328-6480625c9d8e` | unsure | 0.475 |  |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `7661218d-dcc7-4b93-9f40-4298ccc6baed` | unsure | 0.408 |  |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `e2a2e551-5f12-4318-8bd3-4066d9ab6730` | unsure | 0.412 |  |
| PI06 | prompt_injection | instruction plus real human text | 200 | `5418a902-0d36-4c24-81b0-651bfae9f629` | unsure | 0.502 |  |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — |  |
| MF02 | malformed | text is a single character | 400 | `—` | — | — |  |
| MF03 | malformed | text is control characters | 400 | `—` | — | — |  |
| MF04 | malformed | text is only punctuation | 400 | `—` | — | — |  |
| MF05 | malformed | text is a very long single word | 400 | `—` | — | — |  |
| MF06 | malformed | text is emoji only | 400 | `—` | — | — |  |
| MF07 | malformed | text is right-to-left script | 200 | `2cc49b38-353c-45ac-8a09-a00ce0318247` | unsure | 0.703 |  |
| MF08 | malformed | text is 60,000 characters | 413 | `—` | — | — |  |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — |  |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — |  |
| RQ03 | malformed | text is a number | 400 | `—` | — | — |  |
| RQ04 | malformed | text is a list | 400 | `—` | — | — |  |
| RQ05 | malformed | text is null | 400 | `—` | — | — |  |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — |  |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — |  |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — |  |
| RQ09 | malformed | body is empty | 400 | `—` | — | — |  |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — |  |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — |  |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — |  |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 400 | `—` | — | — |  |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — |  |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 0 | 20 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "55b3492f-d8d8-4a85-8fe5-1a96f9b0f4f7",
  "creator_id": "attacker_EV01",
  "guess": "human",
  "confidence": 0.30977815838547235,
  "model_score": 0.1635,
  "style_score": 0.4560563167709447,
  "label": "This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "842d0e13-287f-4aa7-8e95-e6c7b09a0cba",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.5943,
  "style_score": 0.07314560439560447,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "65f438be-3fcf-4cc2-a6c3-84fa5ed1ed22",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.4775631926207605,
  "model_score": 0.6662,
  "style_score": 0.2889263852415211,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "76dadab1-1d10-48ae-aae4-604908eead98",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.525939946975341,
  "model_score": 0.6114,
  "style_score": 0.44047989395068177,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "e154ec7a-560b-4c03-8205-181915e0cabb",
  "creator_id": "attacker_EV05",
  "guess": "human",
  "confidence": 0.26313686920859125,
  "model_score": 0.3212,
  "style_score": 0.20507373841718246,
  "label": "This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "cb3cfded-ebd8-4da1-b02f-0c883139a26b",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.39531739130434784,
  "model_score": 0.5727,
  "style_score": 0.2179347826086957,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "d1a39e14-ea13-490d-bd58-ec42f17e7b7b",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.5431,
  "model_score": 0.5862,
  "style_score": 0.5,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "6f42dfd2-3e9d-4cfc-9802-cfaceec754e7",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.3726,
  "model_score": 0.2452,
  "style_score": 0.5,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "6f26339b-50e3-49ef-814a-c21e36311ee4",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.49293086005513315,
  "model_score": 0.7042,
  "style_score": 0.28166172011026624,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "d4219572-e1e3-4d1c-b62e-573cd313729a",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.8634296286365104,
  "model_score": 0.9792,
  "style_score": 0.747659257273021,
  "label": "This writing shows patterns associated with AI-generated text. A person should review it; this result is not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "ddfdc476-ffd1-4f7b-a212-5de66ec558f2",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.5280441578766563,
  "model_score": 0.6175,
  "style_score": 0.43858831575331253,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "79350416-3802-4340-aa9c-4b497ae82941",
  "creator_id": "attacker_FP02",
  "guess": "unsure",
  "confidence": 0.6456662396768738,
  "model_score": 0.7387,
  "style_score": 0.5526324793537475,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "8f98eafc-c18c-4066-9bac-0c926835bcf1",
  "creator_id": "attacker_FP03",
  "guess": "unsure",
  "confidence": 0.6571218778261401,
  "model_score": 0.8051,
  "style_score": 0.50914375565228,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "3fe86e78-f7b5-418d-8a7a-4b05b06fd706",
  "creator_id": "attacker_FP04",
  "guess": "unsure",
  "confidence": 0.603394948496091,
  "model_score": 0.8329,
  "style_score": 0.3738898969921819,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "616ed947-b754-48db-8f7a-fbcaf1eeb090",
  "creator_id": "attacker_FP05",
  "guess": "unsure",
  "confidence": 0.7115718298565716,
  "model_score": 0.8005,
  "style_score": 0.6226436597131433,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "e88aaee9-ca20-46f3-9ebe-6e3a2289239f",
  "creator_id": "attacker_FP06",
  "guess": "unsure",
  "confidence": 0.5,
  "model_score": 0.8814,
  "style_score": 0.3716421298192864,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "a12f0ca0-0a42-4161-99bc-b35c979fac2f",
  "creator_id": "attacker_FP07",
  "guess": "unsure",
  "confidence": 0.6708769736357645,
  "model_score": 0.8816,
  "style_score": 0.46015394727152886,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_FP08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "7bc90852-4c6d-4900-a8cb-aa52f000b4e0",
  "creator_id": "attacker_PI01",
  "guess": "human",
  "confidence": 0.3254339509587179,
  "model_score": 0.4625,
  "style_score": 0.18836790191743583,
  "label": "This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "9aceac4e-0be5-4f07-b6d5-13b26efc68f7",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.17276029046518415,
  "model_score": 0.2044,
  "style_score": 0.14112058093036828,
  "label": "This writing appears more consistent with human-written text, but an automated assessment cannot establish authorship.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "190cff42-1e4f-4f7e-b328-6480625c9d8e",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.47475701114942115,
  "model_score": 0.5943,
  "style_score": 0.3552140222988422,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "7661218d-dcc7-4b93-9f40-4298ccc6baed",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.40842457667529275,
  "model_score": 0.4998,
  "style_score": 0.31704915335058553,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "e2a2e551-5f12-4318-8bd3-4066d9ab6730",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.41246747852752236,
  "model_score": 0.6401,
  "style_score": 0.1848349570550447,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "5418a902-0d36-4c24-81b0-651bfae9f629",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.5020745113771605,
  "model_score": 0.5583,
  "style_score": 0.4458490227543209,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF06",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "2cc49b38-353c-45ac-8a09-a00ce0318247",
  "creator_id": "attacker_MF07",
  "guess": "unsure",
  "confidence": 0.7032,
  "model_score": 0.9064,
  "style_score": 0.5,
  "label": "We cannot reliably determine how this writing was produced. No conclusion about authorship should be drawn from this result alone.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 413,
  "content_id": null,
  "creator_id": "attacker_MF08",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
