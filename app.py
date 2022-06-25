import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

TRAINING = """
"YOU ate the potato" - it was you who ate it, rather than somebody else
"You ate THE potato" - you ate the important potato, rather than some non-important potato"""


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        prompt = TRAINING + "\n" + request.form["input"]

        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=prompt,
            temperature=float(request.form["temperature"]),
        )
        result = response.choices[0].text
    else:
        result = ""

    input = request.form.get("input", "")
    temperature = request.form.get("temperature", "0.6")
    return render_template("index.html", result=result, input=input, temperature=temperature)
