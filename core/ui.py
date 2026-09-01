import streamlit as st


def inject_css():
    st.markdown(
        """
<style>

/* =========================================================
   WINGMAN DESIGN SYSTEM
   ========================================================= */

:root {
    --wine-950: #1f060e;
    --wine-900: #290711;
    --wine-800: #3b0b18;
    --wine-700: #571126;
    --wine-600: #72152f;

    --red-600: #c92549;
    --red-500: #dd3559;
    --red-400: #eb5774;

    --ink-950: #2a1119;
    --ink-800: #43202b;
    --ink-600: #715a63;
    --ink-500: #88757d;

    --surface: #ffffff;
    --surface-soft: #fbf6f7;
    --surface-tint: #fff1f4;

    --border: #e4d7db;
    --border-strong: #d6c3c9;

    --shadow-sm: 0 5px 18px rgba(52, 10, 24, 0.05);
    --shadow-md: 0 12px 30px rgba(52, 10, 24, 0.08);
    --shadow-lg: 0 20px 45px rgba(52, 10, 24, 0.12);

    --radius-sm: 10px;
    --radius-md: 14px;
    --radius-lg: 20px;
    --radius-xl: 26px;
}


/* =========================================================
   GLOBAL
   ========================================================= */

.stApp {
    background:
        radial-gradient(
            circle at 92% 0%,
            rgba(221, 53, 89, 0.12),
            transparent 25%
        ),
        radial-gradient(
            circle at 0% 100%,
            rgba(114, 21, 47, 0.07),
            transparent 24%
        ),
        linear-gradient(
            135deg,
            #f7f1f3 0%,
            #fcfafb 48%,
            #f8f2f4 100%
        );

    color: var(--ink-950);
}


/* Hide Streamlit chrome */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}


/* Main content */
.main .block-container {
    max-width: 1320px;
    padding: 34px 42px 85px;
}


/* =========================================================
   SIDEBAR
   ========================================================= */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            var(--wine-950) 0%,
            var(--wine-900) 48%,
            #350a17 100%
        );

    border-right: 1px solid rgba(255,255,255,0.07);
}


/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: #fae9ed;
}


/* Sidebar width */
section[data-testid="stSidebar"] > div:first-child {
    padding: 22px 16px 20px;
}


/* Sidebar brand */
section[data-testid="stSidebar"] h2 {
    color: #ffffff !important;
    font-size: 1.22rem !important;
    font-weight: 900 !important;
    letter-spacing: -0.4px;
    margin-bottom: 2px;
}


/* Sidebar captions */
section[data-testid="stSidebar"] .stCaption,
section[data-testid="stSidebar"] small {
    color: #cda3ad !important;
}


/* =========================================================
   SIDEBAR NAVIGATION
   ========================================================= */


/* Every page link */
section[data-testid="stSidebar"] a {
    border-radius: 11px !important;

    padding:
        10px
        11px
        10px
        11px !important;

    margin:
        3px
        0
        3px
        0 !important;

    color: #efdce1 !important;

    font-size: 0.78rem !important;

    font-weight: 650 !important;

    text-decoration: none !important;

    transition:
        background .16s ease,
        color .16s ease,
        transform .16s ease,
        border .16s ease;
}


/* Navigation hover */
section[data-testid="stSidebar"] a:hover {

    background:
        rgba(255,255,255,0.075) !important;

    color: #ffffff !important;

    transform:
        translateX(2px);

}


/* Active navigation */
section[data-testid="stSidebar"] a[aria-current="page"] {

    background:
        linear-gradient(
            90deg,
            rgba(201,37,73,0.34),
            rgba(114,21,47,0.25)
        ) !important;

    border:
        1px solid
        rgba(235,87,116,0.25) !important;

    color: #ffffff !important;

    font-weight: 850 !important;

    box-shadow:
        inset 3px 0 0 var(--red-400),
        0 5px 16px rgba(0,0,0,.12);

}


/* Sidebar divider */
section[data-testid="stSidebar"] hr {
    border-color:
        rgba(255,255,255,0.08) !important;

    margin:
        13px 0
        !important;
}


/* Section headings */
section[data-testid="stSidebar"] .stCaption {
    font-size: .58rem !important;

    font-weight: 900 !important;

    letter-spacing: 1.15px;

    text-transform: uppercase;

    color: #a86f7c !important;
}


/* =========================================================
   TOPBAR
   ========================================================= */

.wm-topbar {

    display: flex;

    justify-content: space-between;

    align-items: center;

    gap: 20px;

    margin-bottom: 30px;

    padding:
        10px
        0
        4px;

}


.wm-topbar-left {
    display: flex;
    align-items: center;
    gap: 10px;
}


.wm-mobile-brand {

    display: inline-flex;

    align-items: center;

    gap: 8px;

    color: var(--wine-800);

    font-size: .8rem;

    font-weight: 850;

}


.wm-topbar-right {

    display: flex;

    align-items: center;

    gap: 8px;

}


.wm-top-pill {

    display: inline-flex;

    align-items: center;

    gap: 7px;

    padding:
        7px
        11px;

    border-radius: 999px;

    background:
        rgba(255,255,255,.76);

    border:
        1px solid
        var(--border);

    color:
        var(--ink-600);

    font-size:
        .58rem;

    font-weight:
        850;

    letter-spacing:
        .55px;

}


.wm-top-pill.online {

    color:
        var(--wine-600);

}


.wm-top-pill.online span {

    width: 6px;

    height: 6px;

    border-radius: 50%;

    background: #4fc785;

}


/* =========================================================
   TYPOGRAPHY
   ========================================================= */

.page-kicker {

    color:
        var(--red-600);

    font-size:
        .64rem;

    font-weight:
        950;

    letter-spacing:
        1.35px;

    text-transform:
        uppercase;

}


.page-title {

    color:
        var(--wine-800);

    font-size:
        clamp(
            2.7rem,
            5vw,
            5.2rem
        );

    font-weight:
        950;

    line-height:
        .92;

    letter-spacing:
        -3.8px;

    margin-top:
        8px;

}


.page-title span {

    color:
        var(--red-500);

}


.page-copy {

    color:
        var(--ink-600);

    max-width:
        820px;

    font-size:
        .95rem;

    line-height:
        1.72;

    margin-top:
        15px;

}


/* Section headings */
.section-head {

    color:
        var(--wine-800);

    font-size:
        1.38rem;

    font-weight:
        950;

    letter-spacing:
        -.45px;

    margin-top:
        30px;

}


.section-sub {

    color:
        var(--ink-500);

    font-size:
        .78rem;

    margin-top:
        3px;

    margin-bottom:
        14px;

}


/* =========================================================
   HERO
   ========================================================= */

.hero {

    margin-top:
        24px;

    padding:
        34px;

    border-radius:
        var(--radius-xl);

    background:
        linear-gradient(
            135deg,
            #320811 0%,
            #5d1028 53%,
            #9e2244 100%
        );

    border:
        1px solid
        rgba(235,87,116,0.35);

    color:
        #ffffff;

    box-shadow:
        var(--shadow-lg);

}


.hero h1,
.hero h2,
.hero h3,
.hero p {

    color:
        #ffffff !important;

}


.hero-muted {

    color:
        #f0ced7 !important;

}


/* =========================================================
   CARDS
   ========================================================= */

.card {

    padding:
        21px;

    border-radius:
        var(--radius-lg);

    background:
        rgba(255,255,255,.98);

    border:
        1px solid
        var(--border);

    box-shadow:
        var(--shadow-sm);

    transition:
        transform .17s ease,
        box-shadow .17s ease,
        border .17s ease;

}


.card:hover {

    transform:
        translateY(-2px);

    border-color:
        var(--border-strong);

    box-shadow:
        var(--shadow-md);

}


.card-tag {

    color:
        var(--red-600);

    font-size:
        .59rem;

    font-weight:
        950;

    letter-spacing:
        .85px;

    text-transform:
        uppercase;

}


.card-title {

    color:
        var(--wine-700);

    font-size:
        1rem;

    font-weight:
        900;

    margin-top:
        7px;

}


.card-copy {

    color:
        var(--ink-600);

    font-size:
        .79rem;

    line-height:
        1.58;

    margin-top:
        6px;

}


/* =========================================================
   METRIC CARDS
   ========================================================= */

.metric-card {

    padding:
        17px 18px;

    border-radius:
        var(--radius-md);

    background:
        #ffffff;

    border:
        1px solid
        var(--border);

    box-shadow:
        var(--shadow-sm);

}


.metric-label {

    color:
        #968089;

    font-size:
        .57rem;

    font-weight:
        900;

    letter-spacing:
        .75px;

    text-transform:
        uppercase;

}


.metric-value {

    color:
        var(--wine-700);

    font-size:
        1.45rem;

    font-weight:
        950;

    letter-spacing:
        -.5px;

    margin-top:
        4px;

}


/* =========================================================
   STREAMLIT CONTAINERS
   ========================================================= */

div[data-testid="stVerticalBlockBorderWrapper"] {

    border:
        1px solid
        var(--border) !important;

    border-radius:
        var(--radius-lg) !important;

    background:
        rgba(255,255,255,.98) !important;

    box-shadow:
        var(--shadow-sm) !important;

}


/* =========================================================
   BUTTONS
   ========================================================= */

.stButton > button,
.stLinkButton > a {

    min-height:
        44px !important;

    border-radius:
        11px !important;

    border:
        1px solid
        var(--border-strong) !important;

    background:
        #ffffff !important;

    color:
        var(--wine-700) !important;

    font-size:
        .76rem !important;

    font-weight:
        850 !important;

    transition:
        transform .16s ease,
        box-shadow .16s ease,
        border .16s ease,
        background .16s ease !important;

}


.stButton > button:hover,
.stLinkButton > a:hover {

    transform:
        translateY(-2px);

    border-color:
        var(--red-600) !important;

    background:
        #fff8fa !important;

    box-shadow:
        0 8px 20px
        rgba(82, 13, 34, .10) !important;

}


/* Primary button */
.stButton > button[kind="primary"] {

    background:
        linear-gradient(
            135deg,
            var(--wine-700),
            var(--red-600)
        ) !important;

    color:
        #ffffff !important;

    border:
        1px solid
        var(--wine-700) !important;

    box-shadow:
        0 9px 20px
        rgba(91, 15, 38, .18);

}


.stButton > button[kind="primary"]:hover {

    background:
        linear-gradient(
            135deg,
            var(--wine-600),
            var(--red-500)
        ) !important;

}


/* =========================================================
   INPUTS
   ========================================================= */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"] {

    border-radius:
        11px !important;

}


.stTextInput input,
.stTextArea textarea {

    border:
        1px solid
        var(--border-strong) !important;

    background:
        #ffffff !important;

    color:
        var(--ink-950) !important;

}


.stTextInput input:focus,
.stTextArea textarea:focus {

    border-color:
        var(--red-500) !important;

    box-shadow:
        0 0 0 2px
        rgba(201,37,73,.10) !important;

}


/* =========================================================
   FILE UPLOADER
   ========================================================= */

[data-testid="stFileUploader"] {

    border-radius:
        16px;

}


[data-testid="stFileUploaderDropzone"] {

    border:
        1px dashed
        #cfb8bf !important;

    border-radius:
        16px !important;

    background:
        #fffafb !important;

}


[data-testid="stFileUploaderDropzone"]:hover {

    border-color:
        var(--red-500) !important;

    background:
        #fff5f7 !important;

}


/* =========================================================
   PROGRESS
   ========================================================= */

.stProgress > div > div > div > div {

    background:
        linear-gradient(
            90deg,
            var(--wine-600),
            var(--red-500)
        ) !important;

}


/* =========================================================
   REPORT PANELS
   ========================================================= */

.dark-panel {

    padding:
        21px;

    border-radius:
        var(--radius-lg);

    background:
        linear-gradient(
            135deg,
            #320811,
            #64132b
        );

    border:
        1px solid
        #7a1a38;

    color:
        #ffffff;

    box-shadow:
        var(--shadow-md);

}


.dark-panel * {

    color:
        #ffffff !important;

}


.soft-panel {

    padding:
        20px;

    border-radius:
        var(--radius-lg);

    background:
        linear-gradient(
            135deg,
            #fff0f4,
            #fff8fa
        );

    border:
        1px solid
        #edced6;

    color:
        #704a57;

}


.reply-card {

    padding:
        19px;

    border-radius:
        var(--radius-md);

    background:
        #ffffff;

    border:
        1px solid
        var(--border);

    box-shadow:
        var(--shadow-sm);

}


.reply-label {

    color:
        var(--red-600);

    font-size:
        .59rem;

    font-weight:
        950;

    letter-spacing:
        .85px;

    text-transform:
        uppercase;

}


.reply-text {

    color:
        var(--ink-800);

    font-size:
        1rem;

    line-height:
        1.55;

    margin-top:
        7px;

}


/* =========================================================
   DATE CARDS
   ========================================================= */

.idea-card {

    min-height:
        235px;

    padding:
        21px;

    border-radius:
        var(--radius-lg);

    background:
        #ffffff;

    border:
        1px solid
        var(--border);

    box-shadow:
        var(--shadow-sm);

    transition:
        transform .17s ease,
        box-shadow .17s ease;

}


.idea-card:hover {

    transform:
        translateY(-2px);

    box-shadow:
        var(--shadow-md);

}


.idea-number {

    color:
        var(--red-600);

    font-size:
        .60rem;

    font-weight:
        950;

    letter-spacing:
        .9px;

}


.idea-title {

    color:
        var(--wine-700);

    font-size:
        1.04rem;

    font-weight:
        900;

    margin-top:
        6px;

}


.idea-copy {

    color:
        var(--ink-600);

    font-size:
        .78rem;

    line-height:
        1.56;

    margin-top:
        8px;

}


/* =========================================================
   ALERTS
   ========================================================= */

div[data-testid="stAlert"] {

    border-radius:
        13px !important;

}


/* =========================================================
   EXPANDERS
   ========================================================= */

details {

    border:
        1px solid
        var(--border) !important;

    border-radius:
        13px !important;

    background:
        #ffffff !important;

}


/* =========================================================
   FOOTER
   ========================================================= */

.footer {

    margin-top:
        55px;

    padding-top:
        20px;

    text-align:
        center;

    color:
        #9a858d;

    font-size:
        .68rem;

}


.footer strong {

    color:
        var(--wine-700);

}


/* =========================================================
   RESPONSIVE
   ========================================================= */

@media (max-width: 900px) {

    .main .block-container {

        padding:
            25px
            20px
            60px;

    }

    .page-title {

        letter-spacing:
            -2.4px;

    }

    .wm-topbar-right {

        display:
            none;

    }

}


@media (max-width: 640px) {

    .main .block-container {

        padding:
            22px
            15px
            55px;

    }

    .page-title {

        font-size:
            2.65rem;

        letter-spacing:
            -2px;

    }

    .hero {

        padding:
            24px;

        border-radius:
            20px;

    }

}

</style>
        """,
        unsafe_allow_html=True,
    )