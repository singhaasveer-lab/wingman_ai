import streamlit as st

from core.ui import inject_css

inject_css()

st.markdown(
    """
<style>
.home-hero{
    padding:34px 36px;
    border-radius:28px;
    background:
        radial-gradient(circle at 85% 15%,rgba(238,78,111,.24),transparent 22%),
        linear-gradient(135deg,#2b0712,#521022 58%,#871d3d);
    color:#fff;
    box-shadow:0 24px 55px rgba(56,8,25,.17);
}
.home-hero h1{
    color:#fff;
    font-size:clamp(2.8rem,5vw,5rem);
    line-height:.92;
    letter-spacing:-3.4px;
    margin:10px 0;
}
.home-hero span{
    color:#ff6d8a;
}
.home-hero p{
    color:#efd0d8;
    max-width:760px;
    line-height:1.7;
}
.home-eyebrow{
    color:#ffbbc9;
    font-size:.62rem;
    font-weight:950;
    letter-spacing:1.2px;
}
.action{
    min-height:220px;
    padding:24px;
    border-radius:22px;
    background:#fff;
    border:1px solid #e4d8dc;
    box-shadow:0 10px 28px rgba(72,15,31,.05);
}
.action-icon{
    font-size:2rem;
}
.action-code{
    color:#a32142;
    font-size:.59rem;
    font-weight:950;
    letter-spacing:.9px;
    margin-top:8px;
}
.action-title{
    color:#4d1224;
    font-size:1.13rem;
    font-weight:950;
    margin-top:6px;
}
.action-copy{
    color:#78666d;
    font-size:.79rem;
    line-height:1.55;
    margin-top:8px;
}
.flow-step{
    padding:17px;
    min-height:132px;
    border-radius:17px;
    background:#fff;
    border:1px solid #e6dadd;
}
.flow-no{
    color:#c92549;
    font-size:.58rem;
    font-weight:950;
}
.flow-title{
    color:#511426;
    font-size:.84rem;
    font-weight:900;
    margin-top:7px;
}
.flow-copy{
    color:#88757c;
    font-size:.69rem;
    line-height:1.45;
    margin-top:5px;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="page-kicker">WINGMAN CONTROL ROOM</div>

<div class="page-title">
    Better decisions.<br>
    <span>Less overthinking.</span>
</div>

<div class="page-copy">
    Wingman turns messy dating situations into structured intelligence,
    actionable decisions and communication you can actually use.
</div>
""",
    unsafe_allow_html=True,
)

st.write("")

st.markdown(
    """
<div class="home-hero">

<div class="home-eyebrow">
PERSONAL DATING INTELLIGENCE
</div>

<h1>
Read the room.<br>
<span>Then move.</span>
</h1>

<p>
One system for screenshots, conversation analysis, replies,
decision support and date planning.
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-head">Choose your mission</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-sub">Start from the decision you are actually trying to make.</div>',
    unsafe_allow_html=True,
)

columns = st.columns(3)

actions = [
    (
        columns[0],
        "01 · INVESTIGATE",
        "📸",
        "Screenshot Intelligence",
        "Upload the real conversation and turn it into Conversation DNA, signals and a next move.",
        "pages/screenshot.py",
    ),
    (
        columns[1],
        "02 · RESPOND",
        "✍️",
        "Reply Lab",
        "Shape your response around intent, energy, boldness and context.",
        "pages/reply_lab.py",
    ),
    (
        columns[2],
        "03 · PLAN",
        "🥂",
        "Date Intelligence",
        "Build a date around vibe, budget, activity and how much time you have.",
        "pages/date_ideas.py",
    ),
]

for col, code, icon, title, copy, page in actions:
    with col:
        st.markdown(
            f"""
<div class="action">
<div class="action-icon">{icon}</div>
<div class="action-code">{code}</div>
<div class="action-title">{title}</div>
<div class="action-copy">{copy}</div>
</div>
""",
            unsafe_allow_html=True,
        )
        st.page_link(
            page,
            label=f"Open {title} →",
            use_container_width=True,
        )

st.markdown(
    '<div class="section-head">How the system thinks</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-sub">The intelligence layer underneath the interface.</div>',
    unsafe_allow_html=True,
)

flow = [
    ("01", "INPUT", "Screenshot or situation"),
    ("02", "EXTRACT", "OCR + conversation parsing"),
    ("03", "MEASURE", "Warmth, reciprocity, engagement"),
    ("04", "GROUND", "Retrieve relevant RAG guidance"),
    ("05", "DECIDE", "Next move + confidence"),
    ("06", "ACT", "Reply or date plan"),
]

cols = st.columns(6)

for col, (num, title, copy) in zip(cols, flow):
    with col:
        st.markdown(
            f"""
<div class="flow-step">
<div class="flow-no">{num}</div>
<div class="flow-title">{title}</div>
<div class="flow-copy">{copy}</div>
</div>
""",
            unsafe_allow_html=True,
        )

st.markdown(
    '<div class="section-head">Wingman signal</div>',
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="soft-panel">
<b>Don't optimize for attention.</b>
<br><br>
Optimize for clarity, reciprocity and the next useful action.
<br><br>
<span style="opacity:.72;">
Response time is context. It is not a verdict.
</span>
</div>
""",
    unsafe_allow_html=True,
)