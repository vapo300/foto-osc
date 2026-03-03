from flask import Flask, request, jsonify
import pytesseract
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route("/ocr", methods=["POST"])
def ocr():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    img = Image.open(BytesIO(file.read()))

    text = pytesseract.image_to_string(img, lang="spa")

    return jsonify({"text": text})

@app.route("/", methods=["GET"])
def home():
    return "OCR server running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
