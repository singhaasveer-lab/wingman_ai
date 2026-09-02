import io
import os
from pathlib import Path

from PIL import Image
import pytesseract


def _configure_tesseract() -> None:
    """
    Configure Tesseract automatically.

    Uses TESSERACT_CMD when provided, then checks common Windows
    installation locations, and finally falls back to PATH.
    """

    env_path = os.getenv("TESSERACT_CMD")

    if env_path and Path(env_path).exists():
        pytesseract.pytesseract.tesseract_cmd = env_path
        return

    common_paths = [
        Path(r"C:\Program Files\Tesseract-OCR\tesseract.exe"),
        Path(r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"),
        Path(r"C:\Users\Public\Tesseract-OCR\tesseract.exe"),
    ]

    for path in common_paths:
        if path.exists():
            pytesseract.pytesseract.tesseract_cmd = str(path)
            return


_configure_tesseract()


def extract_text(image_source):
    """
    Extract text from an image.

    Returns:
        tuple[str, str | None]:
        (extracted_text, message)

    The second value is None on success and contains a readable
    error message when OCR fails.
    """

    try:
        if isinstance(image_source, Image.Image):
            image = image_source

        elif isinstance(image_source, (bytes, bytearray)):
            image = Image.open(io.BytesIO(image_source))

        elif isinstance(image_source, (str, Path)):
            image = Image.open(image_source)

        elif hasattr(image_source, "read"):
            image_source.seek(0)
            image = Image.open(image_source)

        else:
            return "", "Unsupported image input."

        image = image.convert("RGB")

        text = pytesseract.image_to_string(image).strip()

        if not text:
            return "", "OCR completed, but no readable text was detected."

        return text, None

    except pytesseract.TesseractNotFoundError:
        return (
            "",
            "Tesseract OCR was not found. "
            "Wingman checked the standard Windows installation paths.",
        )

    except Exception as exc:
        return "", f"OCR processing failed: {exc}"