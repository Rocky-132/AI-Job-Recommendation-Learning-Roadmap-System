# backend/utils.py

import io
from pypdf import PdfReader

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts raw text content from PDF file bytes.
    """
    try:
        pdf_file = io.BytesIO(file_bytes)
        reader = PdfReader(pdf_file)
        text = ""
        for page_number, page in enumerate(reader.pages):
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception as e:
        # Return empty string if pdf parsing fails, allowing logs/debugging
        print(f"PDF parsing failed: {e}")
        return ""

def extract_text_from_txt(file_bytes: bytes) -> str:
    """
    Decodes txt file content with safe utf-8 handling.
    """
    try:
        return file_bytes.decode("utf-8", errors="ignore")
    except Exception as e:
        print(f"TXT decoding failed: {e}")
        return ""

def extract_text_from_file(file_bytes: bytes, filename: str) -> str:
    """
    Inspects file extension and routes to appropriate text extractor.
    """
    ext = filename.split(".")[-1].lower() if "." in filename else ""
    if ext == "pdf":
        return extract_text_from_pdf(file_bytes)
    elif ext == "txt":
        return extract_text_from_txt(file_bytes)
    else:
        # Try txt decoding as fallback
        return extract_text_from_txt(file_bytes)
