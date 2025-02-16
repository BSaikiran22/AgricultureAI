import os

# Get current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# List contents of the dataset folder
dataset_path = os.path.join(current_dir, "datasets", "weed_dataset")
if os.path.exists(dataset_path):
    print("Contents of 'weed_dataset':", os.listdir(dataset_path))
else:
    print("Dataset folder not found at:", dataset_path)
