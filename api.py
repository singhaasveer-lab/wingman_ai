from fastapi import FastAPI,File,HTTPException,UploadFile
from pydantic import BaseModel,Field
from core.coach import analyze
from core.ocr import extract_text
app=FastAPI(title='Wingman AI API',version='3.0.0',description='Conversation intelligence, screenshot OCR and reply generation.')
class AnalyzeRequest(BaseModel):conversation:str=Field(min_length=1,max_length=15000)
@app.get('/')
def root():return {'name':'Wingman AI','status':'online','version':'3.0.0'}
@app.get('/health')
def health():return {'status':'healthy'}
@app.post('/analyze')
def analyze_route(request:AnalyzeRequest):
    try:return analyze(request.conversation)
    except Exception as exc:raise HTTPException(status_code=500,detail=str(exc)) from exc
@app.post('/analyze-screenshot')
async def screenshot_route(file:UploadFile=File(...)):
    if not file.content_type or not file.content_type.startswith('image/'):raise HTTPException(status_code=400,detail='Upload an image file.')
    data=await file.read()
    class Memory:
        def __init__(self,d):self.d=d
        def getvalue(self):return self.d
    text,msg=extract_text(Memory(data))
    if not text:raise HTTPException(status_code=422,detail=msg)
    return {'message':msg,'extracted_text':text,'analysis':analyze(text)}
