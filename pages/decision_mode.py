import streamlit as st

from core.coach import analyze
from core.db import save_history
from core.ui import inject_css

inject_css()

st.markdown(
    """
<style>
.decision-banner{
    padding:30px;
    border-radius:23px;
    background:#17050c;
    border:1px solid #4d1125;
    color:#fff;
}
.decision-banner h1{
    color:#fff;
    font-size:clamp(2.6rem,4.6vw,4.8rem);
    line-height:.92;
    letter-spacing:-3px;
}
.decision-banner span{
    color:#ef4266;
}
.decision-card{
    padding:24px;
    border-radius:20px;
    background:#fff;
    border:1px solid #e1d5d9;
}
.decision-result{
    padding:27px;
    border-radius:21px;
    background:linear-gradient(135deg,#520f25,#9e2244);
    color:white;
    box-shadow:0 18px 38px rgba(66,8,26,.16);
}
.decision-result h2,
.decision-result p{
    color:#fff!important;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="page-kicker">DECISION INTELLIGENCE</div>

<div class="decision-banner">

<h1>
Don't just ask<br>
<span>what should I say?</span>
</h1>

<p>
Ask the more useful question:
what is the smartest next move?
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-head">Decision input</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):

    situation = st.text_area(
        "Situation",
        height=210,
        placeholder=(
            "We went on a date and it went really well. "
            "They said we should meet again. I texted the next day, "
            "got a short response and now they have not replied. "
            "I am wondering whether I should text again."
        ),
    )

    decision = st.selectbox(
        "What are you deciding?",
        [
            "Should I text?",
            "Should I ask them out?",
            "Should I wait?",
            "Should I clarify something?",
            "Should I move on?",
        ],
    )

    build = st.button(
        "RUN DECISION ENGINE →",
        use_container_width=True,
        type="primary",
    )


if build:

    if not situation.strip():

        st.warning(
            "Give Wingman the situation first."
        )

        st.stop()


    with st.spinner(
        "Evaluating the situation..."
    ):

        result = analyze(
            situation
        )


    vibe = result[
        "vibe_type"
    ]


    if decision == "Should I text?":

        if vibe == "positive":

            recommendation = "YES · SEND ONE GOOD MESSAGE"
            explanation = (
                "The visible interaction has enough momentum. "
                "Focus on quality and direction rather than volume."
            )

        elif vibe == "neutral":

            recommendation = "ONLY IF YOU HAVE A REAL HOOK"
            explanation = (
                "Do not text simply to reduce uncertainty. "
                "Give the other person something meaningful to respond to."
            )

        else:

            recommendation = "NO · GIVE SPACE"
            explanation = (
                "The current visible pattern does not justify "
                "increasing message volume."
            )


    elif decision == "Should I ask them out?":

        if vibe == "positive":

            recommendation = "YES · MAKE IT SPECIFIC"
            explanation = (
                "There is enough positive conversational momentum "
                "to justify a concrete invitation."
            )

        else:

            recommendation = "NOT YET · TEST THE ENERGY"
            explanation = (
                "There is not enough evidence to make escalation "
                "the strongest next move."
            )


    elif decision == "Should I wait?":

        if vibe == "positive":

            recommendation = "WAIT BRIEFLY · THEN MOVE"
            explanation = (
                "The interaction looks healthy enough that patience "
                "is more useful than pressure."
            )

        elif vibe == "neutral":

            recommendation = "WAIT AND WATCH RECIPROCITY"
            explanation = (
                "The evidence is mixed. Let their next level of "
                "effort give you additional information."
            )

        else:

            recommendation = "WAIT"
            explanation = (
                "Pushing harder is unlikely to improve the current signal."
            )


    elif decision == "Should I clarify something?":

        if vibe == "positive":

            recommendation = "CLARIFY DIRECTLY"
            explanation = (
                "Clear communication is better than building a theory "
                "around ambiguous signals."
            )

        else:

            recommendation = "ONLY CLARIFY IF IT MATTERS"
            explanation = (
                "Do not create a heavy conversation around a weak signal."
            )


    else:

        if vibe == "caution":

            recommendation = "STOP ESCALATING"
            explanation = (
                "The visible pattern does not currently justify "
                "additional effort from your side."
            )

        else:

            recommendation = "DON'T MAKE A FINAL CALL YET"
            explanation = (
                "The available evidence is not strong enough "
                "to turn one moment into a permanent conclusion."
            )


    save_history(
        "Decision",
        situation,
        result["vibe"],
        result["confidence"],
    )


    st.session_state.decision_result = {
        "recommendation": recommendation,
        "explanation": explanation,
        "result": result,
    }


output = st.session_state.get(
    "decision_result"
)

if not output:
    st.info(
        "Your decision brief will appear here after the engine runs."
    )
    st.stop()


result = output[
    "result"
]


st.markdown(
    '<div class="section-head">Executive decision</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="decision-result">

<div class="card-tag" style="color:#f39caf;">
WINGMAN'S CALL
</div>

<h2>
{output["recommendation"]}
</h2>

<p>
{output["explanation"]}
</p>

</div>
""",
    unsafe_allow_html=True,
)


a, b, c = st.columns(3)

with a:
    st.metric(
        "Confidence",
        f'{result["confidence"]}%'
    )

with b:
    st.metric(
        "Current vibe",
        result["vibe"]
    )

with c:
    st.metric(
        "Decision",
        result["decision"]
    )


st.markdown(
    '<div class="section-head">Evidence stack</div>',
    unsafe_allow_html=True,
)

for signal in result["signals"]:

    value = int(
        signal["value"] * 100
    )

    st.write(
        f'**{signal["label"]} · {value}%**'
    )

    st.progress(
        value
    )

    st.caption(
        signal["detail"]
    )


st.markdown(
    '<div class="section-head">Why?</div>',
    unsafe_allow_html=True,
)

st.info(
    result["summary"]
)

st.warning(
    result["warning"]
)