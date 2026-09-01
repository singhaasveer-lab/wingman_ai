import streamlit as st

from core.db import initialize_database
from core.ui import inject_css


# ============================================================
# WINGMAN APP CONFIG
# ============================================================

st.set_page_config(
    page_title="Wingman AI",
    page_icon="🥀",
    layout="wide",
    initial_sidebar_state="expanded",
)

initialize_database()
inject_css()


# ============================================================
# PAGE REGISTRY
# ============================================================

PAGES = [
    st.Page(
        "pages/home.py",
        title="Overview",
        icon="🏠",
        default=True,
    ),

    st.Page(
        "pages/screenshot.py",
        title="Screenshot Intelligence",
        icon="📸",
    ),

    st.Page(
        "pages/reply_lab.py",
        title="Reply Lab",
        icon="✍️",
    ),

    st.Page(
        "pages/decision_mode.py",
        title="Decision Mode",
        icon="🎯",
    ),

    st.Page(
        "pages/date_ideas.py",
        title="Date Ideas",
        icon="🥂",
    ),

    st.Page(
        "pages/dating_tips.py",
        title="Dating Intelligence",
        icon="💡",
    ),

    st.Page(
        "pages/saved.py",
        title="Saved",
        icon="❤️",
    ),

    st.Page(
        "pages/history.py",
        title="History",
        icon="🕘",
    ),

    st.Page(
        "pages/how_it_works.py",
        title="How It Works",
        icon="⚙️",
    ),
]


# ============================================================
# HIDE STREAMLIT'S DEFAULT NAVIGATION
# ============================================================

pg = st.navigation(
    PAGES,
    position="hidden",
)


# ============================================================
# CUSTOM WINGMAN SIDEBAR
# ============================================================

with st.sidebar:

    # -------------------------
    # BRAND
    # -------------------------

    st.markdown("## 🥀 Wingman")

    st.caption(
        "Dating intelligence platform"
    )

    st.markdown(
        "🟢 **SYSTEM ONLINE**"
    )

    st.divider()


    # -------------------------
    # COMMAND
    # -------------------------

    st.caption(
        "COMMAND"
    )

    st.page_link(
        "pages/home.py",
        label="Overview",
        icon="🏠",
    )

    st.page_link(
        "pages/screenshot.py",
        label="Screenshot Intelligence",
        icon="📸",
    )

    st.page_link(
        "pages/reply_lab.py",
        label="Reply Lab",
        icon="✍️",
    )

    st.page_link(
        "pages/decision_mode.py",
        label="Decision Mode",
        icon="🎯",
    )

    st.page_link(
        "pages/date_ideas.py",
        label="Date Ideas",
        icon="🥂",
    )

    st.page_link(
        "pages/dating_tips.py",
        label="Dating Intelligence",
        icon="💡",
    )


    # -------------------------
    # LIBRARY
    # -------------------------

    st.markdown("")

    st.caption(
        "LIBRARY"
    )

    st.page_link(
        "pages/saved.py",
        label="Saved",
        icon="❤️",
    )

    st.page_link(
        "pages/history.py",
        label="History",
        icon="🕘",
    )


    # -------------------------
    # SYSTEM
    # -------------------------

    st.markdown("")

    st.caption(
        "SYSTEM"
    )

    st.page_link(
        "pages/how_it_works.py",
        label="How It Works",
        icon="⚙️",
    )


    # -------------------------
    # PRINCIPLE
    # -------------------------

    st.markdown("")

    st.caption(
        "WINGMAN PRINCIPLE"
    )

    st.caption(
        "Read patterns, not single messages."
    )

    st.caption(
        "OCR · RAG · NLP · SQLite"
    )


# ============================================================
# RUN CURRENT PAGE
# ============================================================

pg.run()