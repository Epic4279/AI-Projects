import random
import time

from utils.getkeys import key_check
import pydirectinput
import keyboard
from utils.directkeys import PressKey, ReleaseKey, W, D, A, SPACE

# Sleep time after actions

# Wait for me to push B to start.


# Hold down W no matter what!
def rand_num():
    import keyboard
    from utils.directkeys import PressKey, ReleaseKey, W, D, A, SPACE
    sleepy = 0.1

    # Wait for me to push B to start.
    keyboard.wait('B')
    time.sleep(sleepy)

    # Hold down W no matter what!
    keyboard.press('W')
    while True:
       action = random.randint(0, 3)
       if action == 0:
           print("Action 0: Do nothing, release 'A' and 'D' keys (if held down)")
           ReleaseKey(A)
           ReleaseKey(D)
           time.sleep(sleepy)
       elif action == 1:
           print("Action 1: Hold 'A' (left)")
           PressKey(A)
           time.sleep(sleepy)
           ReleaseKey(A)
       elif action == 2:
           print("Action 2: Hold 'D' (right)")
           PressKey(D)
           time.sleep(sleepy)
           ReleaseKey(D)
       elif action == 3:
           print("Action 3: Press Jump ('space') and release 'A' and 'D'")
           PressKey(SPACE)
           time.sleep(sleepy)
           ReleaseKey(SPACE)
           ReleaseKey(A)
           ReleaseKey(D)
       # Randomly pick action then sleep.
       # 0 do nothing release everything ( except W )
       # 1 hold left
       # 2 hold right
       # 3 Press Jump

       # End simulation by hitting h
       keys = key_check()
       if keys == "H":
           break

    keyboard.release('W')

rand_num()
