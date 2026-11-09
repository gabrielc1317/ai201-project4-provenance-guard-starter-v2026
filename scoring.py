"""
Turning two numbers into one, and one number into something a person can read.
← YOU BUILD THIS IN MILESTONES 4 AND 5

Two functions live here, and both are stubs.

`combine_signals` is where your false-positive decision from Milestone 1
actually gets made. Everything above it — the labels, the appeal path — is
downstream of a number this function produced.

`score_to_label` is where you stop writing for a machine and start writing for
a person. A score of 0.62 means nothing to a writer.

⚠️ Your README's **Signals and Scoring** section has to name the file and
function holding your combining rule. The grader checks your code against what
you claim, so that line should read `scoring.py::combine_signals`.
"""

import config


def combine_signals(model_score: float, style_score: float) -> float:
    """Combine independent AI-likeness scores, guarding disagreement.

    A difference >= config.DISAGREEMENT_THRESHOLD produces the neutral 0.5
    score. Otherwise use the normalized weighted average in config.py.
    """
    import math
    scores = (model_score, style_score)
    if not all(math.isfinite(s) and 0.0 <= s <= 1.0 for s in scores):
        raise ValueError("Signals must be finite floats between 0 and 1")
    if abs(model_score - style_score) >= config.DISAGREEMENT_THRESHOLD:
        return 0.5
    weight_total = config.WEIGHT_MODEL_SIGNAL + config.WEIGHT_STYLE_SIGNAL
    if weight_total <= 0:
        raise ValueError("Combined signal weight must be positive")
    return (
        config.WEIGHT_MODEL_SIGNAL * model_score
        + config.WEIGHT_STYLE_SIGNAL * style_score
    ) / weight_total


def score_to_label(score: float) -> tuple[str, str]:
    """Return classification and reader facing explanation."""
    if score >= config.AI_THRESHOLD:
        return (
            "ai",
            "This writing shows patterns associated with AI-generated text. "
            "A person should review it; this result is not proof of authorship."
        )
    if score <= config.HUMAN_THRESHOLD:
        return (
            "human",
            "This writing appears more consistent with human-written text, "
            "but an automated assessment cannot establish authorship."
        )
    return (
        "unsure",
        "We cannot reliably determine how this writing was produced. "
        "No conclusion about authorship should be drawn from this result alone."
    )


def label_ranges() -> list[tuple[str, str]]:
    """The score range each label covers."""
    return [
        ("high-confidence human", f"0.00 – {config.HUMAN_THRESHOLD:.2f}"),
        ("unsure", f"{config.HUMAN_THRESHOLD:.2f} – {config.AI_THRESHOLD:.2f}"),
        ("high-confidence AI", f"{config.AI_THRESHOLD:.2f} – 1.00"),
    ]
