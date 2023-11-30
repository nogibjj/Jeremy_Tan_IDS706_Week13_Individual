from dotenv import load_dotenv
import os
import requests
import json
import base64

load_dotenv()

from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
)

app = Flask(__name__)
API_TOKEN = os.getenv("API_TOKEN")

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/dandelin/vilt-b32-finetuned-vqa"


@app.route("/")
def index():
    """retruns index page"""
    return render_template("index.html")


@app.route("/not_study", methods=["GET"])
def not_study():
    """returns not study html template"""
    return render_template("not_study.html")


@app.route("/study", methods=["GET"])
def study():
    """returns study html template"""
    return render_template("study.html")


def query(filename):
    """query hugging face inferene api"""
    with open(filename, "rb") as f:
        data = f.read()

    encoded_data = base64.b64encode(data).decode("utf-8")

    payload = {
        "inputs": {
            "question": "is this person studying?",
            "image": encoded_data,
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)
    return json.loads(response.content.decode("utf-8"))


@app.route("/predict", methods=["POST"])
def predict():
    """test predict"""
    file = request.files.get("image")
    print(request.form)
    use_default_image = request.form.get("use_default_image")
    print(use_default_image)
    if use_default_image != "false":
        # Load the default image
        result = query("static/final.jpg")
    else:
        if file and file.filename != "":
            print(file)
            # Save the uploaded file temporarily
            temp_filename = "temp.jpg"
            file.save(temp_filename)

            # Perform the query using the uploaded file
            result = query(temp_filename)

            # Delete the temporary file
            os.remove(temp_filename)
        else:
            return jsonify({"error": "No selected file"}), 400
    yes_answer_score = [item["score"] for item in result if item["answer"] == "yes"]
    no_answer_score = [item["score"] for item in result if item["answer"] == "no"]
    yes_answer_score = yes_answer_score[0] if yes_answer_score else 0
    no_answer_score = no_answer_score[0] if no_answer_score else 0
    # grab results and check
    if no_answer_score > yes_answer_score:
        return redirect(url_for("not_study"))
    return redirect(url_for("study"))


if __name__ == "__main__":
    app.run(debug=True)
