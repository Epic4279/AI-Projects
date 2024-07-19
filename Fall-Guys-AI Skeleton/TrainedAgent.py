import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
import time
import cv2
from utils.grabscreen import grab_screen
from utils.directkeys import PressKey, ReleaseKey, W, D, A, SPACE
from fastai.vision.all import *

def label_func(x):
    return x.parent.name
learn_inf = load_learner(r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data\export.pkl")# Your code here, use load_learner and get the path to the export.pkl
print("loaded learner")

# Sleep time after actions
sleepy = 0.1

# Wait for me to push B to start.
keyboard.wait('B')
time.sleep(sleepy)

# Hold down W no matter what!
keyboard.press('w')

while True:

    image = grab_screen(region=(0, 0, 2560, 1440))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image, (224, 224))
    # cv2.imshow("Fall", image)
    # cv2.waitKey(1)
    start_time = time.time()
    result = learn_inf.predict(image)
    action = result[0]
    # print(result[2][0].item(), result[2][1].item(), result[2][2].item(), result[2][3].item())

    # action = random.randint(0,3)

    if action == "Jump" or result[2][0] > .1:
        print(f"JUMP! - {result[1]}")
        keyboard.press("space")
        keyboard.release("a")
        keyboard.release("d")
        time.sleep(sleepy)

    if action == "Nothing":
        # print("Doing nothing....")
        keyboard.release("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    if action == "Left" or result[2][0] > .1:
        print(f"LEFT! - {result[1]}")
        keyboard.press("a")
        keyboard.release("d")
        keyboard.release("space")
        time.sleep(sleepy)

    if action == "Right" or result[2][0] > .1:
        print(f"Right! - {result[1]}")
        keyboard.press("d")
        keyboard.release("a")
        keyboard.release("space")
        time.sleep(sleepy)

    # Your code here - end simulation by hitting h
    if keyboard.is_pressed('H'):
        break

    print(f"Action: {action}, Prediction Time: {time.time() - start_time:.4f} seconds")

    # Your code here - end simulation by hitting h


keyboard.release('W')