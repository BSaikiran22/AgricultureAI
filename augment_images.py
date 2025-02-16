from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
from PIL import Image
import numpy as np

# Define paths
weed_folder = "datasets/weed_dataset/weeds"
no_weed_folder = "datasets/weed_dataset/no_weeds"

# Data Augmentation Setup
datagen = ImageDataGenerator(
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

def augment_images(folder, save_folder):
    if not os.path.exists(folder):
        print(f"Error: Folder '{folder}' not found!")
        return
    
    images = os.listdir(folder)
    if len(images) == 0:
        print(f"No images found in {folder}!")
        return
    
    print(f"Augmenting images in {folder}...")

    for img_name in images:
        img_path = os.path.join(folder, img_name)
        try:
            img = Image.open(img_path).convert('RGB')
            img = img.resize((128, 128))  # Resize if needed
            img_array = np.array(img).reshape((1, 128, 128, 3))  # Reshape for TensorFlow

            # Generate and save augmented images
            i = 0
            for batch in datagen.flow(img_array, batch_size=1, save_to_dir=save_folder, save_prefix='aug', save_format='jpg'):
                i += 1
                if i >= 5:  # Generate 5 augmented images per original
                    break
            
            print(f"Generated 5 images for {img_name}")
        except Exception as e:
            print(f"Error processing {img_name}: {e}")

# Augment both classes
augment_images(weed_folder, weed_folder)
augment_images(no_weed_folder, no_weed_folder)

print("Augmentation complete!")
