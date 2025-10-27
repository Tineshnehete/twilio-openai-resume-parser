import os, tempfile, requests
from PyPDF2 import PdfReader
import docx
from twilio.request_validator import RequestValidator
from config import TWILIO_AUTH_TOKEN

def extract_text_from_pdf(path):
    reader = PdfReader(path)
    return "\n".join([p.extract_text() or "" for p in reader.pages])

def extract_text_from_docx(path):
    doc = docx.Document(path)
    return "\n".join([p.text for p in doc.paragraphs])

def download_and_extract(media_url, content_type):
    ext = ".pdf" if "pdf" in content_type else ".docx" if "word" in content_type else ""
    r = requests.get(media_url)
    fd, tmp_file = tempfile.mkstemp(suffix=ext)
    with os.fdopen(fd, "wb") as f:
        f.write(r.content)
    text = ""
    if ext == ".pdf":
        text = extract_text_from_pdf(tmp_file)
    elif ext == ".docx":
        text = extract_text_from_docx(tmp_file)
    os.remove(tmp_file)
    return text

def valid_twilio_request(req):
    if not TWILIO_AUTH_TOKEN:
        return True
    validator = RequestValidator(TWILIO_AUTH_TOKEN)
    signature = req.headers.get("X-Twilio-Signature", "")
    return validator.validate(req.url, req.form.to_dict(), signature)
