from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

fortunes = [
    "Your vibe attracts your tribe. Keep shining, fam! ✨",
    "Big moves coming — get ready to glow up! 🚀",
    "Take a breath, sip some tea ☕, and slay the day.",
    "Good energy flows your way when you keep it 100. 💯",
    "Sometimes, the best flex is self-care. Don’t sleep on it! 😴",
    "Your grind is about to pay off. Trust the process! 💪",
    "Manifest those dreams — the universe is lowkey listening. 🌌",
    "Keep your circle tight, your goals tight-er. Squad goals! 👯‍♂️",
    "It’s okay to vibe lowkey sometimes. Recharge and restart. 🔋",
    "Glow up alert: New opportunities are sliding into your DMs! 📩"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fortune')
def fortune():
    return jsonify({"fortune": random.choice(fortunes)})

if __name__ == "__main__":
    app.run(debug=True)
