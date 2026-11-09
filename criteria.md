# Acceptance criteria — Provenance Guard

Five criteria that say what "working" means for this service, written in unit 7
**before** you built it.

**All five are yours.** None are given.

An acceptance criterion names a number or something plainly observable. *"The
detector is accurate"* is an opinion — and perfect AI detection isn't possible
anyway, so it's an opinion about something nobody can deliver. *"Of 10 pieces I
wrote myself, at most 1 is labelled high-confidence AI"* is a criterion.

Under each, write a sentence or two on **why that target**. *"I allow at most 1
false positive in 10 because on a writing site a wrong accusation costs more
than a missed detection"* is a real answer.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

**Cover at least three of these five areas.** They're prompts, not a form.

| Area | A question it could answer |
|---|---|
| False positives | How often may a human's writing get called AI? |
| Score spread | How far apart should clearly-AI and clearly-human text score? |
| Label coverage | Is every one of your three labels actually reachable? |
| The appeal path | Does an appeal always change status and always get recorded? |
| Bad input | What happens when `text` is missing, empty, or enormous? |

Two things worth knowing before you pick numbers:

- **The expensive mistake is one-sided.** Missing some AI text costs the site a
  little. Accusing a real writer costs that person a lot. A criterion that
  treats both errors as equally bad is describing a system nobody would ship.
- **Unit 8 tests across three trials, and the target has to hold across all
  three.** Your first signal runs a model, so identical input can score
  differently twice. A target of "at most 1 in 10" against trials of 2, 1, 2 is
  a **miss**.

---
## 1.

<!-- No more then 5% of verfieid human submissions should be incorrectly labelled as high confidence AI.-->



**Why this target: Being falsely accused of submitting AI-genereated content has serious potential consequences, as a result the amount of verified human submissions that sould be labelled as high confidence AI, should remain relatively low.**



---

## 2.

<!-- There should be a minimum score seperation of 0.3 between AI generated and human written samples.-->



**Why this target: There should be a clear boundary between Ai generated content and human written ones, 0.3 score seperation shows a clear difference between the two while not being so far apart that every run would be labelled as unsure. **



---

## 3.

<!-- All 3  labels should be reachable during a test. -->



**Why this target: There is no reason that a label should not be reachable duriong a test, for the system to work properly all 3 labels muts be available**



---

## 4.

<!-- 100% of appeals should bre recorded. -->



**Why this target: Every appeal should be recorded, for no reason should one be dropped or forgotten, etc. it is crucial that each appeal is recorded for human review so a writer can challenge a false classification.**



---

## 5.

<!-- Out of 10 malformed requests, 10 of them should be rejected correctly without server errors. -->



**Why this target: If theres something wrong with a request whether the text is missing, empty, extremely long, wrong syntax, etc. they should be handled properly (rejected) by the server without error.**



---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 8 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Uncertain cases land in the unsure band

         The system handles uncertain cases well.

         **Why this target:** ...

         > **Revised in unit 8:** Text I judged borderline scores between
         > 0.4 and 0.6 in at least 4 of 5 cases.
         >
         > **Why revised:** "well" gave me nothing to check. I couldn't
         > reach a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "At most 1 of 10 of my own pieces flagged as AI" → "at most 3
            of 10", because 1 of 10 turned out to be hard.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
