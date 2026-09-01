import streamlit as st

from core.rag import retrieve_context
from core.ui import inject_css

inject_css()

st.markdown(
    """
<style>
.editorial-hero{
    padding:27px 29px;
    border-bottom:1px solid #dacbd0;
    margin-bottom:10px;
}
.editorial-hero h1{
    color:#35101d;
    font-size:clamp(2.5rem,4.7vw,4.7rem);
    line-height:.94;
    letter-spacing:-3px;
}
.editorial-hero span{
    color:#c92649;
}
.article-card{
    padding:24px 0;
    border-bottom:1px solid #dfd4d8;
}
.article-category{
    color:#ab2344;
    font-size:.59rem;
    font-weight:950;
    letter-spacing:1px;
}
.article-title{
    color:#461324;
    font-size:1.25rem;
    font-weight:900;
    margin-top:7px;
}
.article-copy{
    color:#6f5b63;
    font-size:.83rem;
    line-height:1.68;
    margin-top:8px;
    max-width:850px;
}
.search-panel{
    padding:21px;
    border-radius:18px;
    background:#2a0a14;
    border:1px solid #511327;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="page-kicker">
    DATING INTELLIGENCE
</div>

<div class="editorial-hero">

<h1>
A better read<br>
<span>on modern dating.</span>
</h1>

<p>
Wingman's knowledge layer retrieves principles for texting, first dates,
flirting, communication and confidence.
</p>

</div>
""",
    unsafe_allow_html=True,
)

topics = [
    "First date",
    "Texting",
    "Flirting",
    "Conversation",
    "Confidence",
    "After the date",
    "Common mistakes",
]

selected = st.selectbox(
    "Browse a category",
    topics,
)


st.markdown(
    '<div class="section-head">Selected intelligence</div>',
    unsafe_allow_html=True,
)

results = retrieve_context(
    selected,
    top_k=5,
)

for item in results:

    st.markdown(
        f"""
<div class="article-card">

<div class="article-category">
{item["category"].upper()}
</div>

<div class="article-title">
{item["title"]}
</div>

<div class="article-copy">
{item["content"]}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


st.markdown(
    '<div class="section-head">Ask the knowledge layer</div>',
    unsafe_allow_html=True,
)

question = st.text_input(
    "Search",
    placeholder=(
        "What should I do if the conversation suddenly goes quiet?"
    ),
)


if question:

    st.markdown(
        '<div class="section-sub">Top retrieved guidance</div>',
        unsafe_allow_html=True,
    )

    matches = retrieve_context(
        question,
        top_k=4,
    )

    for item in matches:

        with st.container(
            border=True
        ):

            a, b = st.columns(
                [4, 1]
            )

            with a:

                st.caption(
                    item["category"].upper()
                )

                st.subheader(
                    item["title"]
                )

                st.write(
                    item["content"]
                )

            with b:

                st.metric(
                    "Relevance",
                    f'{round(item["retrieval_score"] * 100)}%'
                )


st.markdown(
    """
<div class="search-panel">

<div class="card-tag"
     style="color:#ef8fa5;">
WINGMAN PRINCIPLE
</div>

<h3 style="color:white;">
Patterns beat guesses.
</h3>

<p style="color:#dbb6c0;">
One message rarely explains an entire interaction.
Consistency, reciprocity, effort and context are stronger evidence.
</p>

</div>
""",
    unsafe_allow_html=True,
)