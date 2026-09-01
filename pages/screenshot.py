import streamlit as st

from core.coach import analyze
from core.db import save_history, save_item
from core.ocr import extract_text
from core.ui import inject_css

inject_css()

st.markdown(
    """
<style>
.forensic-head{
    padding:27px 29px;
    border-radius:22px;
    background:#241018;
    border:1px solid #52152a;
    color:white;
}
.forensic-head h1{
    color:white;
    font-size:clamp(2.4rem,4vw,4.3rem);
    line-height:.94;
    letter-spacing:-2.8px;
    margin:8px 0;
}
.forensic-head span{
    color:#ef4668;
}
.forensic-head p{
    color:#d9b3be;
    max-width:780px;
    line-height:1.65;
}
.evidence{
    padding:18px;
    border-radius:18px;
    background:#2e131c;
    border:1px solid #541827;
    color:#f8e9ed;
}
.evidence-label{
    color:#ed6280;
    font-size:.58rem;
    font-weight:950;
    letter-spacing:.9px;
}
.evidence-value{
    color:#fff;
    font-size:1.25rem;
    font-weight:900;
    margin-top:5px;
}
.analysis-band{
    padding:21px;
    border-radius:18px;
    background:#fff;
    border:1px solid #e5dadd;
}
.signal-number{
    color:#b52245;
    font-size:1.2rem;
    font-weight:950;
}
.signal-caption{
    color:#8b777e;
    font-size:.67rem;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="forensic-head">

<div class="card-tag" style="color:#f18aa0;">
CONVERSATION FORENSICS
</div>

<h1>
Give me the screenshot.<br>
<span>I'll find the pattern.</span>
</h1>

<p>
Wingman extracts the visible conversation, converts it into measurable
signals and produces a structured recommendation instead of pretending
to know what another person is thinking.
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.write("")

uploaded = st.file_uploader(
    "Upload screenshot",
    type=["png", "jpg", "jpeg", "webp"],
    label_visibility="collapsed",
)

if not uploaded:

    st.markdown(
        """
<div class="analysis-band">

<div class="card-tag">
INPUT PROTOCOL
</div>

<h3>
📸 Upload a conversation screenshot
</h3>

<p>
Best results come from a clear screenshot with visible message text.
Wingman will run OCR before analysis.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.stop()


with st.container(border=True):

    st.markdown(
        '<div class="card-tag">SOURCE IMAGE</div>',
        unsafe_allow_html=True,
    )

    st.image(
        uploaded,
        use_container_width=True,
    )


if st.button(
    "RUN FULL INTELLIGENCE SCAN →",
    use_container_width=True,
    type="primary",
):

    with st.spinner("Extracting visible conversation..."):
        text, message = extract_text(
            uploaded
        )

    if not text:
        st.error(message)
        st.stop()

    with st.expander("OCR result"):
        st.text(text)

    with st.spinner("Analyzing conversational signals..."):
        result = analyze(text)

    st.session_state.last_conversation = text
    st.session_state.last_analysis = result

    save_history(
        "Screenshot",
        text,
        result["vibe"],
        result["confidence"],
    )

    st.rerun()


result = st.session_state.get(
    "last_analysis"
)

if not result:
    st.stop()


st.markdown(
    '<div class="section-head">Signal overview</div>',
    unsafe_allow_html=True,
)

a, b, c, d = st.columns(4)

overview = [
    (a, result["confidence"], "CONFIDENCE"),
    (b, result["decision"], "DECISION"),
    (c, result["vibe"], "VIBE"),
    (d, result["archetype"], "ARCHETYPE"),
]

for col, value, label in overview:
    with col:
        st.markdown(
            f"""
<div class="evidence">
<div class="evidence-label">{label}</div>
<div class="evidence-value">{value}</div>
</div>
""",
            unsafe_allow_html=True,
        )


st.markdown(
    '<div class="section-head">Executive interpretation</div>',
    unsafe_allow_html=True,
)

st.info(
    result["summary"]
)


st.markdown(
    '<div class="section-head">Conversation DNA</div>',
    unsafe_allow_html=True,
)

for signal in result["signals"]:

    value = int(
        signal["value"] * 100
    )

    left, right = st.columns(
        [5, 1]
    )

    with left:

        st.write(
            f'**{signal["label"]}**'
        )

        st.progress(
            value
        )

        st.caption(
            signal["detail"]
        )

    with right:

        st.markdown(
            f"""
<div class="signal-number">
{value}%
</div>
<div class="signal-caption">
signal
</div>
""",
            unsafe_allow_html=True,
        )


st.markdown(
    '<div class="section-head">Decision brief</div>',
    unsafe_allow_html=True,
)

st.markdown(
    f"""
<div class="soft-panel">

<div class="card-tag">
NEXT BEST MOVE
</div>

<h3>
{result["next_move"]}
</h3>

<p>
{result["reasoning"]}
</p>

</div>
""",
    unsafe_allow_html=True,
)


st.markdown(
    '<div class="section-head">RAG evidence</div>',
    unsafe_allow_html=True,
)

for item in result["rag_results"]:

    with st.container(border=True):

        st.caption(
            item["category"].upper()
        )

        st.subheader(
            item["title"]
        )

        st.write(
            item["content"]
        )

        st.caption(
            f'Retrieval relevance: '
            f'{round(item["retrieval_score"] * 100)}%'
        )


st.markdown(
    '<div class="section-head">Response matrix</div>',
    unsafe_allow_html=True,
)

styles = [
    ("😎 CONFIDENT", "confident"),
    ("🔥 FLIRTY", "flirty"),
    ("😂 FUNNY", "funny"),
    ("💜 SWEET", "sweet"),
    ("🧊 CHILL", "chill"),
]

for label, key in styles:

    with st.container(border=True):

        st.markdown(
            f'<div class="reply-label">{label}</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="reply-text">{result["replies"][key]}</div>',
            unsafe_allow_html=True,
        )

        if st.button(
            f"Save {key}",
            key=f"save_reply_{key}",
            use_container_width=True,
        ):

            save_item(
                "Screenshot Reply",
                label,
                result["replies"][key],
            )

            st.toast(
                "Saved."
            )


if st.button(
    "✍️ Continue in Reply Lab →",
    use_container_width=True,
):

    st.switch_page(
        "pages/reply_lab.py"
    )


st.warning(
    result["warning"]
)