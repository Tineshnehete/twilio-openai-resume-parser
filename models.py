from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

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
