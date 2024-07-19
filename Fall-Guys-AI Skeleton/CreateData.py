import numpy as np
import cv2
import time
import os
# from RandomAgent import rand_num
from utils.grabscreen import grab_screen
import random
from utils.getkeys import key_check
import pydirectinput

def get_data(file_name, file_name2):
    # Retrieve data from path and return the data (x and y) in lists called image_data and targets.
    if os.path.isfile(file_name) and os.path.isfile(file_name2):
        image_data = np.load(file_name, allow_pickle=True).tolist()
        targets = np.load(file_name2, allow_pickle=True).tolist()
    else:
        image_data = []
        targets = []

    return image_data, targets


def save_data(file_name, file_name2, image_data, targets):
    # Use np to save the data into filename1 and filename2
    np.save(file_name, np.array(image_data, dtype=object))
    np.save(file_name2, np.array(targets, dtype=object))


def preprocess_image(image):
    # Convert to grayscale
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    image_canny = cv2.Canny(image_gray, threshold1=119, threshold2=250)

    # Resize image
    image_resized = cv2.resize(image_canny, (224, 224))

    return image_resized


def collect_data(image_data, targets):
    while True:
        # Start collecting data upon a certain key press"""

        # Capture screen using grab_screen with a specified region
        screen = grab_screen(region=(0, 0, 2560, 1440))

        # Preprocess captured image
        processed_image = preprocess_image(screen)

        # Convert processed image to numpy array and append to image_data
        image_data.append(processed_image)

        # Record current key presses and append to targets
        # action = rand_num()
        # targets.append(action)

    return image_data, targets


# def display_images(image_data):
#     for i, image in enumerate(image_data):
#         if isinstance(image, np.ndarray):
#             window_title = f"Image {i}"
#             cv2.imshow(window_title, image)
#             cv2.waitKey(1)  # Display each image for 500ms
#         else:
#             print(f"Skipping non-array image at index {i}")
#     cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage:
    file_name = r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data\training_dat.npy"
    file_name2 = r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data\target_dat.npy"

    image_data, targets = get_data(file_name, file_name2)
    # print(f"image_data={image_data}")
    # print(f"targets={targets}")
    # image_data, targets = collect_data(image_data, targets)
    while True:
        keys = key_check()
        if 'B' in keys:
            break

    while True:
        last_time = time.time()
        # Grab screen using grab_screen
        image = grab_screen(region=(0, 0, 2560, 1440))
        # Convert to grayscale
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(image.dtype)  # Print image dtype here
        # Apply Canny edge detection
        image = cv2.Canny(image, threshold1=119, threshold2=250)
        # Resize the image
        image = cv2.resize(image, (224, 224))

        # Convert to numpy array and store in image_data
        image = np.array(image)
        image_data.append(image)

        # Record current key presses
        keys = key_check()

        targets.append(keys)

        # Break upon a certain key press
        if 'H' in keys:
            break

        print('loop took {} seconds'.format(time.time() - last_time))

    save_data(file_name, file_name2, image_data, targets)

    #display_images(image_data)
