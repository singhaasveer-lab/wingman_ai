from io import BytesIO
from PIL import Image,ImageEnhance,ImageFilter
import pytesseract

def extract_text(file):
    try:
        image=Image.open(BytesIO(file.getvalue())).convert('L')
        image=image.resize((image.width*2,image.height*2))
        image=ImageEnhance.Contrast(image).enhance(1.6)
        image=image.filter(ImageFilter.SHARPEN)
        text=pytesseract.image_to_string(image,config='--psm 6').strip()
        return (text,'Screenshot successfully converted to text.') if text else ('','No readable conversation was detected. Try a clearer screenshot.')
    except pytesseract.pytesseract.TesseractNotFoundError:
        return '','Tesseract OCR is not installed or is not on PATH. Install it on Windows, restart VS Code, and retry.'
    except Exception as exc:return '',f'Screenshot processing failed: {exc}'
