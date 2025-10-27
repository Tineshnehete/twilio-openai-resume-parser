from flask import Blueprint, request, jsonify
from helpers import valid_twilio_request, download_and_extract
from .langchain import extract_fields_with_langchain
from models import db, Candidate

twilio_bp = Blueprint("twilio", __name__)

@twilio_bp.route("/twilio/webhook", methods=["POST"])
def twilio_webhook():
#     if not valid_twilio_request(request):
#         return "Invalid signature", 403

    data = request.form
    text_content = data.get("Body", "")
    from_number = data.get("From")
    num_media = int(data.get("NumMedia", 0))
    resume_text = text_content

    if num_media > 0:
        media_url = data.get("MediaUrl0")
        content_type = data.get("MediaContentType0", "")
        resume_text += "\n" + download_and_extract(media_url, content_type)

    parsed = extract_fields_with_langchain(resume_text)
    
    parsed["source"] = f"WhatsApp {from_number}"

    candidate = Candidate(**parsed)
    db.session.add(candidate)
    db.session.commit()

    return jsonify({"status": "saved", "data": parsed})

@twilio_bp.route("/candidates")
def list_candidates():
    all_cands = Candidate.query.order_by(Candidate.created_at.desc()).all()
    return jsonify([
        {
            "id": c.id, "name": c.name, "email": c.email,
            "phone": c.phone, "skills": c.skills,
            "source": c.source, "created_at": str(c.created_at)
        } for c in all_cands
    ])
