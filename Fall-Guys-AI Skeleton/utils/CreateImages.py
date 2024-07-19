import cv2
import numpy as np
import os
data = np.load(r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data\training_dat.npy", allow_pickle=True)
targets = np.load(r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data\target_dat.npy", allow_pickle=True)
print(targets[:5])
print(f'Image Data Shape: {data.shape}')
print(f'targets Shape: {targets.shape}')

# Verify lengths match
if len(data) != len(targets):
    raise ValueError("Lengths of data and targets do not match.")

# Let's see how many of each type of move we have.
unique_elements, counts = np.unique(targets, return_counts=True)
print(np.asarray((unique_elements, counts)))

# Store both data and targets in a list.
# We may want to shuffle down the road.

#4 Data Target Pairing
holder_list = []
for i, image in enumerate(data):
    holder_list.append([data[i], targets[i]])


# Step 5: Image Writing
# Create a directory to save the images if it doesn't exist
data_dir = r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data"
if not os.path.exists(data_dir):
    os.makedirs(data_dir)


# Action Counters dictionary
action_counts = {
    'Up': 0,
    'Left': 0,
    'Right': 0,
    'Jump': 0
}

# Loop through holder_list to save images
for image, target in holder_list:
    if target == "W":
        action_name = 'Up'
    elif target == "A":
        action_name = 'Left'
    elif target == "D":
        action_name = 'Right'
    elif target == '':
        action_name = 'Jump'
    else:
        continue  # Skip if action is not recognized

    # Increment the counter for the current action
    action_counts[action_name] += 1

    # Generate the filename
    images_file = f"{action_name}_{action_counts[action_name]}.png"
    filepath = os.path.join(data_dir, images_file)
    if image.dtype != np.uint8:
        image = image.astype(np.uint8)
    # Save the image
    cv2.imwrite(filepath, image)

    print(f"Saved {images_file}")
