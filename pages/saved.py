import streamlit as st

from core.db import delete_saved, get_saved
from core.ui import inject_css

inject_css()


# ============================================================
# PAGE HEADER
# ============================================================

st.markdown(
    """
<div class="page-kicker">
    REPLY VAULT
</div>

<div class="page-title">
    Keep the good ones.<br>
    <span>Lose the panic.</span>
</div>

<div class="page-copy">
    Your saved replies live here. Keep the lines that feel like you,
    remove the ones that no longer fit, and come back when you need them.
</div>
""",
    unsafe_allow_html=True,
)


items = get_saved()


# ============================================================
# EMPTY STATE
# ============================================================

if not items:

    st.markdown(
        """
<div class="hero">

<div class="card-tag" style="color:#f3b5c2;">
REPLY VAULT · EMPTY
</div>

<h2>
Nothing saved yet.
</h2>

<p class="hero-muted">
Build a response in Screenshot Intelligence or Reply Lab,
then save the ones worth keeping.
</p>

</div>
""",
        unsafe_allow_html=True,
    )

    st.write("")

    a, b = st.columns(2)

    with a:
        st.page_link(
            "pages/screenshot.py",
            label="📸 Analyze a conversation →",
            use_container_width=True,
        )

    with b:
        st.page_link(
            "pages/reply_lab.py",
            label="✍️ Open Reply Lab →",
            use_container_width=True,
        )

    st.stop()


# ============================================================
# SUMMARY
# ============================================================

a, b, c = st.columns(3)

with a:

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-label">
SAVED RESPONSES
</div>

<div class="metric-value">
{len(items)}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with b:

    categories = set(
        str(item["category"])
        for item in items
    )

    st.markdown(
        f"""
<div class="metric-card">

<div class="metric-label">
STRATEGIES
</div>

<div class="metric-value">
{len(categories)}
</div>

</div>
""",
        unsafe_allow_html=True,
    )


with c:

    st.markdown(
        """
<div class="metric-card">

<div class="metric-label">
STORAGE
</div>

<div class="metric-value"
     style="font-size:1rem;">
LOCAL SQLITE
</div>

</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# FILTER
# ============================================================

st.markdown(
    """
<div class="section-head">
    Your library
</div>

<div class="section-sub">
    Filter the vault by strategy when you need something specific.
</div>
""",
    unsafe_allow_html=True,
)

categories = [
    "All",
] + sorted(
    set(
        str(item["category"])
        for item in items
    )
)

selected_category = st.selectbox(
    "Filter",
    categories,
)


filtered = (
    items
    if selected_category == "All"
    else [
        item
        for item in items
        if str(item["category"]) == selected_category
    ]
)


# ============================================================
# SAVED ITEMS
# ============================================================

for item in filtered:

    with st.container(
        border=True
    ):

        left, right = st.columns(
            [5, 1]
        )

        with left:

            st.markdown(
                f"""
<div class="reply-label">
{item["category"]}
</div>

<div class="reply-text"
     style="font-size:1.05rem;">
“{item["content"]}”
</div>
""",
                unsafe_allow_html=True,
            )

            st.caption(
                f'Saved {item["created_at"]}'
            )


        with right:

            if st.button(
                "🗑 Remove",
                key=f"delete_{item['id']}",
                use_container_width=True,
            ):

                delete_saved(
                    item["id"]
                )

                st.toast(
                    "Removed from your vault."
                )

                st.rerun()


# ============================================================
# FOOTER CTA
# ============================================================

st.write("")

st.markdown(
    """
<div class="soft-panel">

<b>
Your best reply is usually the one that still sounds like you.
</b>

<br><br>

Use the vault for inspiration, not scripts.

</div>
""",
    unsafe_allow_html=True,
)