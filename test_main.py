"""
Test goes here

"""
import os
from dotenv import load_dotenv
import requests


load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"


def test_html_files(directory="templates/"):
    """checks html files exists"""
    html_files = [f for f in os.listdir(directory) if f.endswith(".html")]

    for html_file in html_files:
        file_path = os.path.join(directory, html_file)
        assert os.path.exists(file_path) and os.path.isfile(file_path)


def test_api():
    """checks hugging api token works"""
    test_payload = {"inputs": "The answer to the universe is [MASK]."}
    response = requests.post(API_URL, headers=HEADERS, json=test_payload)
    assert response.status_code == 200


if __name__ == "__main__":
    test_html_files()
    test_api()
