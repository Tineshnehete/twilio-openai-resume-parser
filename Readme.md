Here’s a clean, developer-friendly **README.md** for your Flask + LangChain Resume Parser demo 👇

---

# 🧠 AI Resume Parser (Flask + LangChain)

A simple demo system that automatically extracts details such as **name, email, phone number, and skills** from resumes or text messages received via WhatsApp or API.
It uses **Flask**, **LangChain**, and **SQLAlchemy** for intelligent text parsing and structured data storage.

---

## 🚀 Features

* 📥 Accepts messages or resume files (PDF, DOCX)
* 🧩 Uses **LangChain** with **OpenAI** model for smart data extraction
* 💾 Stores structured data in a **SQLAlchemy (SQLite)** database
* 🔗 Ready for integration with **Twilio WhatsApp Webhook**
* ⚙️ Modular and extendable architecture

---

## 🧾 Flow Summary

```
WhatsApp Message 
   ↓
Twilio Webhook 
   ↓
Flask API (/twilio/webhook)
   ↓
LangChain (OpenAI Model)
   ↓
Extracted Data (name, email, phone, skills)
   ↓
SQLAlchemy Database (Candidate Table)

```
---

## 🧱 Project Structure

```
resume_parser/
├── app.py                 
├── config.py              
├── models.py             
├── integrations/
├   ├── langchain.py
├   └── twilio.py
├── helpers.py
├── requirements.txt     
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/Tineshnehete/twilio-openai-resume-parser
cd twilio-openai-resume-parser
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # for macOS/Linux
venv\Scripts\activate     # for Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
TWILIO_AUTH_TOKEN=your_twilio_auth_token
DATABASE_URL=sqlite:///data.db
```

### 5. Run the Flask app

```bash
python app.py
```

---

## 🧩 Integration Example — Twilio WhatsApp Webhook

The `/twilio/webhook` endpoint can automatically handle incoming WhatsApp messages with resume text or attachments.
Once received:

1. The file is downloaded (PDF or DOCX)
2. Text is extracted using `PyPDF2` or `python-docx`
3. LangChain model parses the resume
4. Data is saved to the database

---

## 🧠 LangChain Prompt

The AI uses a custom prompt to ensure structured JSON output:

```text
You are a professional resume parser.
Extract the following details from the text.

Return **only JSON** with these keys:
name, email, phone, skills, suitable_job_roles, years_of_experience, education_level, work_experience, certifications, summary
Example : {{
  "name": "...",
  "email": "...",
  "phone": "...",
  "skills": "...",
  "suitable_job_roles": "..." -> Text,
  "years_of_experience": "...",
  "education_level": "...",
  "work_experience": "..." -> Text ,
  "certifications": "...",
  "summary": "..."  
}}

Text:
{text}
```

---

## 🗃️ Database Model (SQLAlchemy)

```python
class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(50))
    skills = db.Column(db.Text)
    source = db.Column(db.String(100))
    suitable_job_roles = db.Column(db.Text)
    years_of_experience = db.Column(db.Text)
    education_level = db.Column(db.String(100))
    work_experience = db.Column(db.Text)
    certifications = db.Column(db.Text)
    summary = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

```

---

## 📊 Endpoints Summary

| Endpoint          | Method | Description                                 |
| ----------------- | ------ | ------------------------------------------- |
| `/twilio/webhook` | POST   | Handles incoming WhatsApp messages (Twilio) |
| `/health`         | GET    | Health check endpoint                       |

---

## 🧠 Tech Stack

* **Backend:** Flask
* **Database:** SQLAlchemy (SQLite)
* **AI/NLP:** LangChain + OpenAI
* **File Parsing:** PyPDF2, python-docx
* **Integration:** Twilio WhatsApp API


## 👨‍💻 Author

**Tinesh Nehete**
*Software Developer | AI & SaaS Builder*
📧 [namaste@tineshnehete.com](mailto:namaste@tineshnehete.com)
