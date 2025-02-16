# 🌱 Agriculture AI

## 📌 Project Overview
Agriculture AI is a machine learning-based project designed to help farmers and researchers detect and classify weeds in agricultural fields. The model processes images of crops and weeds to provide accurate predictions, assisting in precision farming and effective weed management.

## 🚀 Features
- 🌾 **Weed Detection**: Identify weeds from crop images using a deep learning model.
- 📊 **Machine Learning Model**: Trained using TensorFlow and Keras.
- 📸 **Image Processing**: Uses OpenCV for preprocessing agricultural images.
- 📱 **Android Integration**: App-based interface for users to upload and analyze images.
- 🌐 **Web App Deployment**: Flask-based web interface for weed detection.
- ☁️ **Cloud Support**: Can be deployed on cloud platforms for scalability.

## 🔧 Installation & Setup
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/BSaikiran22/AgricultureAI.git
cd AgricultureAI
```

### 2️⃣ Install Dependencies
Make sure you have Python installed, then install the required libraries:
```bash
pip install -r requirements.txt
```

### 3️⃣ Download Dataset
Ensure you have the dataset in `datasets/weed_dataset/`.

### 4️⃣ Train the Model
To train the model, run:
```bash
python train.py
```

### 5️⃣ Run the Application
For Web App (Flask):
```bash
python app.py
```
For Android App: Load the `apk` file and install it on your device.

## 💾 Model Details
- **Architecture**: CNN-based model (TensorFlow/Keras)
- **Dataset**: Weed classification dataset
- **Accuracy**: ~90% on test images

## 🔥 How to Use
1. Upload an image of a plant.
2. The model classifies it as either **Weed** or **No Weed**.
3. Provides recommendations for weed control.

## 📂 Project Structure
```
AgricultureAI/
│── models/                     # Trained models stored here
│── datasets/                    # Weed dataset
│── static/                      # Static assets (CSS, JS)
│── templates/                   # HTML templates for Flask app
│── app.py                        # Flask API
│── train.py                      # Training script
│── requirements.txt              # Required Python packages
│── README.md                     # Project documentation
```

## 📌 Future Enhancements
- 🚀 Improve model accuracy with more training data.
- 📡 Deploy on cloud (AWS/GCP/Azure).
- 🤖 Integrate IoT sensors for real-time weed detection.

## 👨‍💻 Contributors
- **Baikadi Sai Kiran Goud** ([@BSaikiran22](https://github.com/BSaikiran22))

## 📜 License
This project is open-source under the **MIT License**.

