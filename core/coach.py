import re
from collections import Counter

from core.rag import retrieve_context


POSITIVE_WORDS = {
    "love", "like", "liked", "fun", "funny", "cute",
    "sweet", "haha", "lol", "great", "amazing", "perfect",
    "nice", "yes", "sure", "definitely", "excited",
    "miss", "missed", "good", "glad",
    "😊", "😍", "😘", "😂", "❤️", "😉", "😏", "🔥"
}

NEGATIVE_WORDS = {
    "no", "nah", "nope", "busy", "stop", "leave",
    "whatever", "fine", "okay", "annoyed", "tired",
    "sorry", "don't", "dont", "can't", "cant", "later"
}

FLIRTY_WORDS = {
    "cute", "handsome", "beautiful", "pretty", "miss",
    "date", "kiss", "trouble", "dangerous", "love",
    "😉", "😏", "😘", "❤️"
}

QUESTION_WORDS = {
    "who", "what", "when", "where",
    "why", "how", "which"
}


def _words(text):
    return re.findall(
        r"[A-Za-z']+|[😂🤣😊😍😘😏😉❤️🔥]",
        str(text).lower(),
    )


def _lines(text):
    return [
        line.strip()
        for line in str(text).splitlines()
        if line.strip()
    ]


def _sentiment(text):
    tokens = _words(text)

    positive = sum(
        token in POSITIVE_WORDS
        for token in tokens
    )

    negative = sum(
        token in NEGATIVE_WORDS
        for token in tokens
    )

    total = positive + negative

    if total == 0:
        return 0.0

    return (positive - negative) / total


def _question_score(text):
    tokens = _words(text)

    score = (
        sum(
            token in QUESTION_WORDS
            for token in tokens
        ) * 0.45
        + str(text).count("?") * 0.55
    )

    return min(
        score / 4,
        1.0,
    )


def _flirt_score(text):
    tokens = _words(text)

    return min(
        sum(
            token in FLIRTY_WORDS
            for token in tokens
        ) / 3,
        1.0,
    )


def _reciprocity_score(text):
    sender_counts = Counter()

    for line in _lines(text):

        if ":" not in line:
            continue

        sender = line.split(
            ":",
            1,
        )[0].strip()

        if sender:
            sender_counts[sender] += 1

    if len(sender_counts) < 2:
        return 0.45

    values = sorted(
        sender_counts.values(),
        reverse=True,
    )[:2]

    return min(
        values[1] /
        max(values[0], 1)
        + 0.15,
        1.0,
    )


def _energy_score(text):
    message_lines = _lines(text)

    if not message_lines:
        return 0.0

    average_length = (
        sum(len(line) for line in message_lines)
        / len(message_lines)
    )

    return min(
        average_length / 70,
        1.0,
    )


def _classify(
    sentiment,
    reciprocity,
    flirt,
    questions,
):

    score = (
        sentiment * 0.35
        + reciprocity * 0.30
        + flirt * 0.20
        + questions * 0.15
    )

    if score >= 0.50:
        return (
            "🟢 Positive momentum",
            "positive",
        )

    if score >= 0.25:
        return (
            "🟡 Mixed but workable",
            "neutral",
        )

    return (
        "🔴 Low / cautious energy",
        "caution",
    )


def _confidence(
    sentiment,
    reciprocity,
    flirt,
    questions,
    message_count,
):

    score = (
        abs(sentiment) * 25
        + reciprocity * 25
        + flirt * 15
        + questions * 10
        + min(
            message_count / 12,
            1,
        ) * 25
    )

    return int(
        max(
            50,
            min(
                95,
                round(score),
            ),
        )
    )


def _build_summary(
    vibe_type,
    reciprocity,
    questions,
):

    if vibe_type == "positive":

        return (
            "The conversation shows enough positive participation "
            "to justify staying engaged. The strongest signal is not "
            "one emoji or one fast reply. It is the repeated evidence "
            "that both people are contributing to the interaction."
        )

    if vibe_type == "neutral":

        return (
            "There is some usable momentum, but the evidence is mixed. "
            "The right move is neither aggressive escalation nor "
            "prematurely assuming the conversation is dead."
        )

    return (
        "The visible conversation contains caution signals. "
        "Trying to increase message volume is unlikely to solve that. "
        "Give the interaction space and watch for voluntary effort."
    )


def _build_next_move(
    vibe_type,
    reciprocity,
    questions,
):

    if vibe_type == "positive":

        return (
            "Move from conversation to direction.",
            (
                "Keep the playful energy, then create a concrete opening. "
                "A specific plan is more useful than several additional "
                "messages that simply keep the chat alive."
            ),
        )

    if vibe_type == "neutral":

        if questions < 0.25:

            return (
                "Change the rhythm, not the message volume.",
                (
                    "Give them one specific, easy-to-answer hook. "
                    "Then let their level of participation tell you "
                    "whether there is genuine momentum."
                ),
            )

        return (
            "Match the energy and test for reciprocity.",
            (
                "There is some engagement, but not enough evidence to "
                "over-invest. Give them an opening and see whether they "
                "choose to carry part of the conversation."
            ),
        )

    return (
        "Back off and let reciprocity reveal itself.",
        (
            "More messages cannot manufacture interest. Give the "
            "interaction room and look for voluntary re-engagement."
        ),
    )


def _build_replies(vibe_type):

    if vibe_type == "positive":

        return {
            "confident":
                "You’re making this way too easy for me 😏",

            "flirty":
                "Careful, keep talking like that and I’m actually taking you out.",

            "funny":
                "Okay, this conversation is getting suspiciously entertaining 😂",

            "sweet":
                "Not gonna lie, I actually like talking to you.",

            "chill":
                "Alright, your turn. Tell me something I wouldn’t guess about you.",
        }

    if vibe_type == "neutral":

        return {
            "confident":
                "Okay, I’m curious now. What’s your most controversial opinion?",

            "flirty":
                "I was going to behave, but you’re making that difficult 😌",

            "funny":
                "Important question: are you always this difficult or am I special? 😂",

            "sweet":
                "Honestly, I like hearing what’s going on in your head. Tell me more.",

            "chill":
                "Fair enough 😌 What are you getting up to today?",
        }

    return {
        "confident":
            "No pressure. I’ll let you do your thing and we can pick this up later.",

        "flirty":
            "I’ll stop being a menace for now 😌",

        "funny":
            "Alright, I’m retiring from my professional texting career 😂",

        "sweet":
            "No worries. Take your time and have a good one.",

        "chill":
            "All good. Catch you later.",
    }


def analyze(text):

    text = str(text).strip()

    if not text:
        return None

    sentiment = _sentiment(text)

    questions = _question_score(text)

    flirt = _flirt_score(text)

    reciprocity = _reciprocity_score(text)

    energy = _energy_score(text)

    message_lines = _lines(text)

    vibe, vibe_type = _classify(
        sentiment,
        reciprocity,
        flirt,
        questions,
    )

    confidence = _confidence(
        sentiment,
        reciprocity,
        flirt,
        questions,
        len(message_lines),
    )

    rag_results = retrieve_context(
        text,
        top_k=3,
    )

    next_move, reasoning = _build_next_move(
        vibe_type,
        reciprocity,
        questions,
    )

    signals = [

        {
            "label": "Warmth",
            "value": max(
                0,
                min(
                    1,
                    0.5
                    + sentiment * 0.35,
                ),
            ),
            "detail":
                "Balance of positive and negative language.",
        },

        {
            "label": "Reciprocity",
            "value": reciprocity,
            "detail":
                "Balance of visible participation between speakers.",
        },

        {
            "label": "Engagement",
            "value": questions,
            "detail":
                "Presence of questions and conversational hooks.",
        },

        {
            "label": "Flirt energy",
            "value": flirt,
            "detail":
                "Playful or explicitly flirt-coded language.",
        },

        {
            "label": "Message energy",
            "value": energy,
            "detail":
                "Approximate richness of the visible messages.",
        },

    ]

    if vibe_type == "positive":

        archetype = (
            "Playful + reciprocal + ready for direction"
        )

    elif vibe_type == "neutral":

        archetype = (
            "Mixed energy + moderate engagement"
        )

    else:

        archetype = (
            "Low momentum + caution required"
        )

    if vibe_type == "positive":

        decision = (
            "MOVE FORWARD"
        )

    elif vibe_type == "neutral":

        decision = (
            "TEST THE ENERGY"
        )

    else:

        decision = (
            "GIVE SPACE"
        )

    return {

        "vibe":
            vibe,

        "vibe_type":
            vibe_type,

        "confidence":
            confidence,

        "archetype":
            archetype,

        "decision":
            decision,

        "summary":
            _build_summary(
                vibe_type,
                reciprocity,
                questions,
            ),

        "signals":
            signals,

        "next_move":
            next_move,

        "reasoning":
            reasoning,

        "replies":
            _build_replies(
                vibe_type,
            ),

        "rag_results":
            rag_results,

        "rag_note":
            (
                rag_results[0]["content"]
                if rag_results
                else
                "Focus on consistency, reciprocity and observable effort."
            ),

        "warning":
            (
                "Wingman cannot know another person's private thoughts. "
                "Use patterns of consistency, reciprocity and effort "
                "instead of treating one message as proof."
            ),

    }