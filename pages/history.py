import streamlit as st

from core.db import get_history
from core.ui import inject_css

inject_css()


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    """
<div class="page-kicker">
    INTELLIGENCE HISTORY
</div>

<div class="page-title">
    See the pattern.<br>
    <span>Not the moment.</span>
</div>

<div class="page-copy">
    Wingman keeps a local timeline of your previous analyses so you can
    look back at situations instead of repeatedly reacting to the same one.
</div>
""",
    unsafe_allow_html=True,
)


rows = get_history()


# ============================================================
# EMPTY STATE
# ============================================================

if not rows:

    st.markdown(
        """
<div class="hero">

<div class="card-tag" style="color:#f3b5c2;">
INTELLIGENCE HISTORY
</div>

<h2>
No history yet.
</h2>

<p class="hero-muted">
Once you analyze a screenshot or run Decision Mode,
your sessions will appear here.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    if st.button(
        "📸 Run your first analysis →",
        use_container_width=True,
        type="primary",
    ):

        st.switch_page(
            "pages/screenshot.py"
        )

    st.stop()


# ============================================================
# CALCULATE SUMMARY
# ============================================================

total = len(rows)

confidence_values = [
    int(row["confidence"])
    for row in rows
    if row["confidence"] is not None
]

average_confidence = (
    round(
        sum(confidence_values)
        / len(confidence_values)
    )
    if confidence_values
    else 0
)

input_types = {}

for row in rows:

    key = str(
        row["input_type"]
    )

    input_types[key] = (
        input_types.get(
            key,
            0,
        )
        + 1
    )


# ============================================================
# SUMMARY CARDS
# ============================================================

a, b, c = st.columns(3)


with a:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-label">
ANALYSES
</div>

<div class="metric-value">
{total}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with b:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-label">
AVG CONFIDENCE
</div>

<div class="metric-value">
{average_confidence}%
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with c:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-label">
INPUT TYPES
</div>

<div class="metric-value">
{len(input_types)}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# BREAKDOWN
# ============================================================

st.markdown(
    """
<div class="section-head">
    Activity breakdown
</div>

<div class="section-sub">
    What Wingman has been used for.
</div>
""",
    unsafe_allow_html=True,
)


cols = st.columns(
    max(
        1,
        min(
            4,
            len(input_types),
        ),
    )
)


for index, (
    input_type,
    count,
) in enumerate(
    input_types.items()
):

    with cols[
        index % len(cols)
    ]:

        st.markdown(
            f"""
<div class="metric-card">

<div class="metric-label">
{input_type}
</div>

<div class="metric-value">
{count}
</div>

</div>
""",
            unsafe_allow_html=True,
        )


# ============================================================
# TIMELINE
# ============================================================

st.markdown(
    """
<div class="section-head">
    Analysis timeline
</div>

<div class="section-sub">
    Most recent sessions first.
</div>
""",
    unsafe_allow_html=True,
)


for index, row in enumerate(rows):

    confidence = (
        int(row["confidence"])
        if row["confidence"] is not None
        else 0
    )


    with st.container(
        border=True
    ):

        a, b, c = st.columns(
            [1.2, 2.5, 1]
        )


        with a:

            st.caption(
                "INPUT"
            )

            st.write(
                row["input_type"]
            )


        with b:

            st.markdown(
                f"""
<div class="reply-label">
VIBE
</div>

<div class="reply-text"
     style="font-size:.98rem;">
{row["vibe"]}
</div>
""",
                unsafe_allow_html=True,
            )


        with c:

            st.metric(
                "Confidence",
                f"{confidence}%",
            )


        st.write(
            row["source_preview"]
        )


        st.caption(
            row["created_at"]
        )


# ============================================================
# PATTERN NOTE
# ============================================================

st.markdown(
    """
<div class="section-head">
    Wingman's reminder
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="soft-panel">

<b>
History is useful because one interaction rarely tells the whole story.
</b>

<br><br>

Look for repeated patterns across time:
reciprocity, consistency, effort and direction.

</div>
""",
    unsafe_allow_html=True,
)