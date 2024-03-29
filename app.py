from flask import Flask, render_template, request, jsonify
from skimage.metrics import structural_similarity
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    # Get the uploaded images from the request
    original_image = request.files['originalImage']
    tampered_image = request.files['tamperedImage']

    # Read the images using OpenCV
    original_image_data = np.frombuffer(original_image.read(), np.uint8)
    tampered_image_data = np.frombuffer(tampered_image.read(), np.uint8)

    original = cv2.imdecode(original_image_data, cv2.IMREAD_GRAYSCALE)
    tampered = cv2.imdecode(tampered_image_data, cv2.IMREAD_GRAYSCALE)

    # Calculate SSIM score
    (score, _) = structural_similarity(original, tampered, full=True)

    # Determine result based on SSIM score
    result_text = "Document is not tampered" if score <= 0.15 else "Document is tampered"

    # Return the result as JSON
    return jsonify(ssim_score=score, result_text=result_text)

if __name__ == '__main__':
    app.run(debug=True)
