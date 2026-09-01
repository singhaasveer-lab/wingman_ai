import streamlit as st

from core.date_engine import build_plan
from core.ui import inject_css

inject_css()

st.markdown(
    """
<style>
.date-hero{
    padding:31px;
    border-radius:25px;
    background:
        radial-gradient(circle at 85% 15%,rgba(236,88,104,.16),transparent 23%),
        linear-gradient(135deg,#fff7f4,#fff,#f9edf0);
    border:1px solid #eadbde;
}
.date-hero h1{
    color:#481527;
    font-size:clamp(2.6rem,4.8vw,4.8rem);
    line-height:.94;
    letter-spacing:-3px;
}
.date-hero span{
    color:#c72b4c;
}
.date-card{
    min-height:245px;
    padding:23px;
    border-radius:20px;
    background:#fff;
    border:1px solid #e3d7da;
    box-shadow:0 11px 28px rgba(80,21,34,.05);
}
.date-num{
    color:#bb2547;
    font-size:.59rem;
    font-weight:950;
    letter-spacing:1px;
}
.date-title{
    color:#511426;
    font-size:1.06rem;
    font-weight:950;
    margin-top:7px;
}
.date-copy{
    color:#77656c;
    font-size:.79rem;
    line-height:1.58;
    margin-top:8px;
}
.date-price{
    margin-top:17px;
    color:#77152f;
    font-weight:900;
}
</style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    """
<div class="page-kicker">
    DATE INTELLIGENCE
</div>

<div class="date-hero">

<h1>
Plan the night.<br>
<span>Leave room for the story.</span>
</h1>

<p>
Wingman builds dates around the actual situation: relationship stage,
vibe, budget, activity level and available time.
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-head">Build your date profile</div>',
    unsafe_allow_html=True,
)

with st.container(border=True):

    a, b, c = st.columns(3)

    with a:

        who = st.selectbox(
            "Situation",
            [
                "First date",
                "New crush",
                "Someone I'm already dating",
                "Partner",
                "Double date",
            ],
        )

    with b:

        vibe = st.selectbox(
            "Vibe",
            [
                "Playful",
                "Romantic",
                "Low-key",
                "Creative",
                "Foodie",
                "Adventurous",
                "Conversation-heavy",
            ],
        )

    with c:

        budget = st.selectbox(
            "Budget",
            [
                "Under ₹500",
                "₹500–₹1,000",
                "₹1,000–₹2,000",
                "₹2,000–₹4,000",
                "₹4,000+",
            ],
        )


    a, b = st.columns(2)

    with a:

        energy = st.slider(
            "Activity level",
            0,
            10,
            6,
        )

    with b:

        time_available = st.selectbox(
            "Time available",
            [
                "60–90 minutes",
                "2–3 hours",
                "Half day",
                "Full evening",
            ],
        )


    objective = st.selectbox(
        "What should the date achieve?",
        [
            "Get to know them",
            "Break the awkwardness",
            "Make it memorable",
            "Keep it casual",
            "Celebrate something",
        ],
    )


    build = st.button(
        "BUILD MY DATE →",
        use_container_width=True,
        type="primary",
    )


if build:

    st.session_state.date_plan = {
        "who": who,
        "vibe": vibe,
        "budget": budget,
        "energy": energy,
        "time": time_available,
        "objective": objective,
        "ideas": build_plan(
            vibe,
            energy,
        ),
    }


plan = st.session_state.get(
    "date_plan"
)

if not plan:
    st.info(
        "Build a profile above and Wingman will create the route."
    )
    st.stop()


st.markdown(
    f"""
<div class="soft-panel">

<div class="card-tag">
WINGMAN DATE PROFILE
</div>

<h3>
{plan["who"]} · {plan["vibe"]}
</h3>

<p>
{plan["budget"]} · {plan["time"]} · {plan["objective"]}
</p>

</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="section-head">Your date architecture</div>',
    unsafe_allow_html=True,
)

labels = [
    ("01", "OPEN"),
    ("02", "SHARED MOMENT"),
    ("03", "OPTIONAL EXTENSION"),
]

cols = st.columns(3)

for col, (num, label), item in zip(
    cols,
    labels,
    plan["ideas"][:3],
):

    title, reason, price = item

    with col:

        st.markdown(
            f"""
<div class="date-card">

<div class="date-num">
{num} · {label}
</div>

<div class="date-title">
{title}
</div>

<div class="date-copy">
{reason}
</div>

<div class="date-price">
{price}
</div>

</div>
""",
            unsafe_allow_html=True,
        )


st.markdown(
    '<div class="section-head">How Wingman would run it</div>',
    unsafe_allow_html=True,
)

a, b, c = st.columns(3)

for col, title, copy in [
    (
        a,
        "START EASY",
        "The opening should remove pressure, not create it. Let both people settle into the interaction.",
    ),
    (
        b,
        "CREATE A SHARED MOMENT",
        "An activity gives you something to react to together and keeps the conversation from becoming an interview.",
    ),
    (
        c,
        "READ THE ROOM",
        "The extension is optional. Continue because both people want to, not because the plan says so.",
    ),
]:

    with col:

        st.markdown(
            f"""
<div class="card">

<div class="card-tag">
{title}
</div>

<div class="card-copy">
{copy}
</div>

</div>
""",
            unsafe_allow_html=True,
        )

st.success(
    "Wingman rule: structure the evening, don't script it."
)