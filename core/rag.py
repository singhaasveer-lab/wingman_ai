import json
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
KB=Path(__file__).resolve().parents[1]/'knowledge_base.json'
def retrieve_context(query,top_k=3):
    with KB.open('r',encoding='utf-8') as f: docs=json.load(f)
    texts=[f"{d['title']} {d['category']} {d['content']} {' '.join(d.get('tags',[]))}" for d in docs]
    if not texts:return []
    v=TfidfVectorizer(lowercase=True,stop_words='english',ngram_range=(1,2),sublinear_tf=True)
    m=v.fit_transform(texts); q=v.transform([str(query)]); s=cosine_similarity(q,m).flatten(); idx=s.argsort()[::-1][:top_k]
    return [{**docs[i],'retrieval_score':float(s[i])} for i in idx]
