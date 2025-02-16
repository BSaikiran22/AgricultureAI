import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model

# Set paths
dataset_path = "datasets/weed_dataset"
model_path = "models/weed_detection_model.keras"

# ✅ Image Data Preprocessing with Augmentation
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os

# Correct dataset path
dataset_path = "datasets/weed_dataset"

# Fix ImageDataGenerator
datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    validation_split=0.2  # ✅ Correctly split training & validation (80%/20%)
)

# Load training data
train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='training'  # ✅ Ensure this is 'training'
)

# Load validation data
val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=(128, 128),
    batch_size=32,
    class_mode='binary',
    subset='validation'  # ✅ Ensure this is 'validation'
)

# Check if validation data is empty
if len(val_data) == 0:
    raise ValueError("🚨 Error: Validation dataset is empty! Add more images.")

print("✅ Dataset loaded successfully!")

# ✅ Use Pre-trained MobileNetV2 Model
base_model = MobileNetV2(input_shape=(128, 128, 3), include_top=False, weights='imagenet')
base_model.trainable = False  # Freeze pretrained layers

# ✅ Add Custom Layers on Top (Fix: Connect the layers properly)
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.3)(x)  # Reduce overfitting
x = Dense(1, activation='sigmoid')(x)  # Binary classification

# ✅ Define Model Correctly
model = Model(inputs=base_model.input, outputs=x)

# ✅ Compile Model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# ✅ Train Model
model.fit(train_data, validation_data=val_data, epochs=10)

# ✅ Save Model
os.makedirs("models", exist_ok=True)
model.save(model_path)

print("Weed detection model trained and saved successfully!")
