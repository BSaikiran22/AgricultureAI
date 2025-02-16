import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image

# Load the trained model
model = tf.keras.models.load_model("models/weed_detection_model.h5")

# Path to the test image
image_path = r"C:\Users\SAI\Downloads\Agriculture_AI_Project_Complete\datasets\weed_dataset\weeds\aug_0_1448.jpg"
  # Change this to your test image path

# Load and preprocess the image
img = image.load_img(image_path, target_size=(128, 128))  # Resize to match training size
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions for batch processing
img_array /= 255.0  # Normalize pixel values

# Make a prediction
prediction = model.predict(img_array)

# Interpret the result
class_labels = ["No Weeds", "Weeds"]  # Adjust according to your dataset
predicted_class = class_labels[int(prediction[0][0] > 0.5)]  # Assuming binary classification

print(f"🔍 Prediction: {predicted_class}")
