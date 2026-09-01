import streamlit as st
from core.coach import analyze
from core.db import save_history,save_item
from core.ui import inject_css
inject_css()
st.markdown('<div class="page-kicker">CONVERSATION COACH</div><div class="page-title">Read the <span>room.</span></div><div class="page-copy">Paste a conversation or describe what happened. Screenshot input lives on the dedicated Screenshot Intelligence page.</div>',unsafe_allow_html=True)
text=st.text_area('Conversation',value=st.session_state.get('coach_text',''),height=230,placeholder='Me: You always disappear 😂\nThem: Maybe I like keeping you curious\nMe: Is that your way of flirting?')
st.session_state.coach_text=text
if st.button('🥀 READ THE ROOM →',use_container_width=True,type='primary'):
    if not text.strip():st.warning('Give Wingman some context first.');st.stop()
    with st.spinner('Wingman is reading the conversation...'):result=analyze(text)
    st.session_state.coach_result=result;save_history('Text',text,result['vibe'],result['confidence']);st.rerun()
r=st.session_state.get('coach_result')
if r:
    st.markdown('## 🥀 Intelligence report');a,b,c=st.columns(3)
    with a:st.markdown(f'<div class="dark-panel"><div class="card-tag">OVERALL READ</div><h2>{r["vibe"]}</h2><p>Confidence: <b>{r["confidence"]}%</b></p></div>',unsafe_allow_html=True)
    with b:st.markdown(f'<div class="metric-card"><div class="metric-label">Confidence</div><div class="metric-value">{r["confidence"]}%</div></div>',unsafe_allow_html=True)
    with c:st.markdown(f'<div class="metric-card"><div class="metric-label">Reply modes</div><div class="metric-value">{len(r["replies"])}</div></div>',unsafe_allow_html=True)
    st.markdown('### 🧠 Executive read');st.info(r['summary'])
    st.markdown('### 📊 Conversation DNA')
    for s in r['signals']:
        v=int(s['value']*100);st.write(f'**{s["label"]} · {v}%**');st.progress(v);st.caption(s['detail'])
    st.markdown('### 🎯 Wingman’s call');st.markdown(f'<div class="soft-panel"><b>{r["next_move"]}</b><br><br>{r["reasoning"]}</div>',unsafe_allow_html=True)
    st.markdown('### 📚 RAG grounding');st.markdown(f'<div class="card"><div class="card-tag">RETRIEVED GUIDANCE</div><div class="card-copy">{r["rag_note"]}</div></div>',unsafe_allow_html=True)
    st.markdown('### ✍️ Reply Lab preview');cols=st.columns(2)
    for i,(label,key) in enumerate([('😎 Confident','confident'),('🔥 Flirty','flirty'),('😂 Funny','funny'),('💜 Sweet','sweet'),('🧊 Chill','chill')]):
        with cols[i%2]:
            with st.container(border=True):
                st.caption(label);st.write(r['replies'][key])
                if st.button(f'❤️ Save {key}',key=f'c_{key}',use_container_width=True):save_item('Coach Reply',label,r['replies'][key]);st.toast('Saved.')
    st.warning(r['warning'])
