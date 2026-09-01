import streamlit as st
from core.ui import inject_css
inject_css()
st.markdown('<div class="page-kicker">SYSTEM DESIGN</div><div class="page-title">How <span>Wingman</span> works.</div><div class="page-copy">A modular pipeline connects screenshot OCR, local retrieval, conversational signal analysis, response construction and local persistence.</div>',unsafe_allow_html=True)
for col,tag,title,text in zip(st.columns(3),['INPUT','INTELLIGENCE','ACTION'],['📸 Screenshot Intelligence','🧠 RAG + NLP','✍️ + 🥂'],['OCR turns the visible chat into conversation text.','Local retrieval grounds guidance while observable signals drive analysis.','Wingman produces reply options, next moves and date structures.']):
    with col:st.markdown(f'<div class="card"><div class="card-tag">{tag}</div><div class="card-title">{title}</div><div class="card-copy">{text}</div></div>',unsafe_allow_html=True)
st.markdown('## Architecture')
st.code('''WINGMAN AI
    |
+---+------------+-------------+
|                |             |
v                v             v
SCREENSHOT   REPLY LAB    DATE IDEAS
   |             |             |
  OCR            |        plan generator
   +------+------+-------------+
          |
          v
   Conversation text
          |
          v
   Signal extraction
          |
      +---+---+
      |   |   |
      v   v   v
    Warmth Reciprocity Flirt
          |
          v
      Vibe engine
          |
     +----+----+
     |         |
     v         v
   Local RAG  Replies
     |         |
     +----+----+
          v
        SQLite''',language='text')
st.info('Wingman interprets observable conversation patterns. It does not claim certainty about another person’s private thoughts or feelings.')
