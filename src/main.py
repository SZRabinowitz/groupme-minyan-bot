import os
from flask import Flask, request, jsonify
import requests


bot_id = os.getenv("bot_id")
app = Flask(__name__)


@app.post("/minyanim")
def index():
    body = request.get_json()
    if body.get("text", "").startswith("/minyan"):
        send_message(fake_minyan_data())
    return jsonify({"Success": True}, 200)


def send_message(text):
    resp = requests.post(
        "https://api.groupme.com/v3/bots/post",
        json={"bot_id": bot_id, "text": text},
    )
    print(resp.status_code, resp.text)


def fake_minyan_data():
    data = """
Shul1: 12:00 Mincha
Shul2: 4:00 Mincha
Shul3: 9:00 Maariv"""
    return data
