import osweeds_path = "datasets/weed_dataset/weeds/"no_weeds_path = "datasets/weed_dataset/no_weeds/"# Check if the directories exist before counting filesif os.path.exists(weeds_path) and os.path.exists(no_weeds_path):    print("Weeds:", len(os.listdir(weeds_path)))    print("No Weeds:", len(os.listdir(no_weeds_path)))else:    print("Error: One or both directories do not exist! Check your dataset path.")