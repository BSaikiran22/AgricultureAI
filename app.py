import os
import numpy as np
import joblib
from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename  # ✅ Corrected import

# Initialize Flask app
app = Flask(__name__)

# Load the trained models
ml_model = joblib.load("models/crop_yield_model.pkl")  # Ensure the model is loaded properly

try:
    dl_model = load_model("models/weed_detection_model.h5")  # Load deep learning model for weed detection
except Exception as e:
    dl_model = None  # Handle case where the model is not found

# Define routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict_yield', methods=['POST'])
def predict_yield():
    try:
        # Get input data from the request
        data = request.get_json()
        features = np.array([[data['temperature'], data['humidity'], data['rainfall']]])  # Ensure correct shape
        
        # Predict crop yield using the machine learning model
        prediction = ml_model.predict(features)
        
        # Return the predicted yield
        return jsonify({'predicted_yield': float(prediction[0])})  # Convert numpy float to regular float

    except Exception as e:
        # Return error message if any exception occurs
        return jsonify({'error': f'Error predicting yield: {str(e)}'})

@app.route('/detect_weed', methods=['POST'])
def detect_weed():
    if dl_model is None:
        # Handle case where the weed detection model is not loaded
        return jsonify({'error': 'Weed detection model not found. Please train and load it first.'})

    try:
        # Ensure file is provided in the request
        if 'image' not in request.files:
            return jsonify({'error': 'No file uploaded. Please upload an image for weed detection.'})

        file = request.files['image']
        filename = secure_filename(file.filename)
        file_path = os.path.join("uploads", filename)
        file.save(file_path)

        # Preprocess the image for weed detection
        img = image.load_img(file_path, target_size=(128, 128))  # Resize to (128, 128)
        img_array = image.img_to_array(img)  # Convert image to array
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension for model input
        img_array /= 255.0  # Normalize image to range [0, 1]

        # Make a prediction with the deep learning model
        prediction = dl_model.predict(img_array)

        # Assuming the model outputs a probability of the presence of weeds
        weed_detected = bool(prediction[0][0] > 0.5)  # Assuming output > 0.5 indicates weed

        return jsonify({'weed_detected': weed_detected})  # Return the result of detection (True/False)

    except Exception as e:
        # Return error message if any exception occurs
        return jsonify({'error': f'Error detecting weed: {str(e)}'})

if __name__ == '__main__':
    os.makedirs("uploads", exist_ok=True)  # Ensure upload folder exists
    os.makedirs("models", exist_ok=True)   # Ensure models folder exists
    app.run(debug=True)  # Start the Flask app
