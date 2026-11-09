"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """Coefficient of variation in sentence lengths (higher = more varied)."""
    lengths = [len(words(sentence)) for sentence in sentences(text)]
    lengths = [count for count in lengths if count]
    if len(lengths) < 2:
        return 0.0
    mean = statistics.mean(lengths)
    return statistics.stdev(lengths) / mean if mean else 0.0


def type_token_ratio(text: str) -> float:
    """Unique lowercase words divided by total words."""
    tokens = words(text)
    return len(set(tokens)) / len(tokens) if tokens else 0.0


def punctuation_density(text: str) -> float:
    """Punctuation marks per word (not necessarily capped at one)."""
    tokens = words(text)
    if not tokens:
        return 0.0
    marks = sum(char in '.,;:!?—–-()[]' for char in text)
    return marks / len(tokens)


# ── Combining them ───────────────────────────────────────────────────────────

def style_signal(text: str) -> float:
    """Heuristic AI-likeness score from surface statistics, in [0, 1]."""
    tokens = words(text)
    if len(tokens) < 20 or len(sentences(text)) < 2:
        return 0.5

    spread = sentence_length_spread(text)
    diversity = type_token_ratio(text)
    punct = punctuation_density(text)

    # Higher variation/diversity/punctuation is tentatively more human-like.
    # Normalization constants are engineering hypotheses, not calibrated facts.
    spread_ai = 1.0 - min(spread / 0.8, 1.0)
    diversity_ai = 1.0 - min(max((diversity - 0.45) / 0.40, 0.0), 1.0)
    punctuation_ai = 1.0 - min(punct / 0.25, 1.0)
    return max(0.0, min(1.0,
        0.45 * spread_ai + 0.35 * diversity_ai + 0.20 * punctuation_ai
    ))


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
