import os

# Paths to dataset folders
weed_folder = "datasets/weed_dataset/weeds"
no_weed_folder = "datasets/weed_dataset/no_weeds"

# Check if directories exist
if not os.path.exists(weed_folder) or not os.path.exists(no_weed_folder):
    print("Error: One or both directories do not exist! Check your dataset path.")
else:
    # Count images
    print("Weeds:", len(os.listdir(weed_folder)))
    print("No Weeds:", len(os.listdir(no_weed_folder)))
