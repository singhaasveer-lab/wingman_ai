import streamlit as st

from core.db import save_item
from core.ui import inject_css

inject_css()

st.markdown(
    """
<style>
.lab-shell{
    padding:28px;
    border-radius:23px;
    background:#fff;
    border:1px solid #e2d7da;
    box-shadow:0 14px 34px rgba(64,12,27,.05);
}
.lab-preview{
    padding:25px;
    border-radius:20px;
    background:linear-gradient(135deg,#fff5f7,#ffffff);
    border:1px solid #efd6dc;
}
.lab-preview-label{
    color:#b12346;
    font-size:.59rem;
    font-weight:950;
    letter-spacing:1px;
}
.lab-message{
    color:#3e1b26;
    font-size:1.35rem;
    line-height:1.5;
    font-weight:750;
    margin-top:11px;
}
.control{
    padding:18px;
    border-radius:17px;
    background:#faf6f7;
    border:1px solid #e6dbde;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="page-kicker">REPLY LAB</div>

<div class="page-title">
    Say it right.<br>
    <span>Without sounding scripted.</span>
</div>

<div class="page-copy">
    The response is the smallest part of the problem. Intent, timing,
    energy and context matter just as much.
</div>
""",
    unsafe_allow_html=True,
)

analysis = st.session_state.get(
    "last_analysis"
)

if not analysis:

    st.markdown(
        """
<div class="lab-preview">

<div class="lab-preview-label">
NO ACTIVE CONVERSATION
</div>

<h3>
Start with a screenshot analysis.
</h3>

<p>
Wingman will carry the conversation context into Reply Lab automatically.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.page_link(
        "pages/screenshot.py",
        label="📸 Open Screenshot Intelligence →",
        use_container_width=True,
    )

    st.stop()


st.markdown(
    f"""
<div class="lab-preview">

<div class="lab-preview-label">
CURRENT SIGNAL
</div>

<div class="lab-message"
style="font-size:1rem;">
{analysis["vibe"]}
</div>

<p>
{analysis["summary"]}
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-head">Compose your strategy</div>',
    unsafe_allow_html=True,
)

a, b = st.columns(2)

with a:

    intent = st.selectbox(
        "Intent",
        [
            "Keep the conversation going",
            "Flirt without overdoing it",
            "Ask them out",
            "Recover from an awkward moment",
            "Be confident without chasing",
            "End the conversation gracefully",
        ],
    )

with b:

    tone = st.selectbox(
        "Communication style",
        [
            "Confident",
            "Flirty",
            "Funny",
            "Sweet",
            "Chill",
        ],
    )


a, b = st.columns(2)

with a:

    boldness = st.slider(
        "Boldness",
        1,
        10,
        6,
    )

with b:

    length = st.select_slider(
        "Length",
        [
            "Short",
            "Natural",
            "Detailed",
        ],
        value="Natural",
    )


if st.button(
    "BUILD RESPONSE →",
    use_container_width=True,
    type="primary",
):

    reply = analysis["replies"][
        tone.lower()
    ]

    if tone == "Flirty" and boldness >= 8:

        reply = (
            reply.rstrip(".")
            + " I think you know exactly what you're doing 😏"
        )

    elif tone == "Confident" and boldness >= 8:

        reply = (
            reply.rstrip(".")
            + " So when are we fixing that?"
        )

    elif tone == "Funny" and boldness >= 8:

        reply = (
            reply.rstrip(".")
            + " I'm starting to think this was your plan all along 😂"
        )

    elif tone == "Sweet" and boldness <= 3:

        reply = (
            "No pressure 😊 "
            + reply
        )

    if length == "Short":

        reply = (
            reply.split(".")[0]
            .strip()
        )

    st.session_state.reply_lab_result = {
        "reply": reply,
        "tone": tone,
        "intent": intent,
        "boldness": boldness,
    }


response = st.session_state.get(
    "reply_lab_result"
)

if not response:
    st.stop()


st.markdown(
    '<div class="section-head">Draft</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):

    st.markdown(
        f"""
<div class="lab-preview">

<div class="lab-preview-label">
{response["tone"].upper()}
</div>

<div class="lab-message">
{response["reply"]}
</div>

<p>
{response["intent"]} · boldness {response["boldness"]}/10
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    a, b = st.columns(2)

    with a:
        if st.button(
            "❤️ Save",
            use_container_width=True,
        ):
            save_item(
                "Reply Lab",
                f'{response["tone"]} · {response["intent"]}',
                response["reply"],
            )
            st.toast("Saved.")

    with b:
        if st.button(
            "↻ Rework",
            use_container_width=True,
        ):
            st.session_state.pop(
                "reply_lab_result",
                None,
            )
            st.rerun()


st.markdown(
    '<div class="section-head">Strategy matrix</div>',
    unsafe_allow_html=True,
)

for label, key in [
    ("CONFIDENT", "confident"),
    ("FLIRTY", "flirty"),
    ("FUNNY", "funny"),
    ("SWEET", "sweet"),
    ("CHILL", "chill"),
]:

    with st.container(border=True):

        st.markdown(
            f'<div class="reply-label">{label}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="reply-text">{analysis["replies"][key]}</div>',
            unsafe_allow_html=True,
        )