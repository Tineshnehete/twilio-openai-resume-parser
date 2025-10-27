from config import create_app
from models import db
from integrations.twilio import twilio_bp

app = create_app()
app.register_blueprint(twilio_bp)

@app.route("/health")
def health():
    return "ok"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port=5000)
