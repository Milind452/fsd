# STEP 1: Keep track of time
# STEP 2: Trigger some action every 2 hours
# STEP 3: Perform action representing a break

import webbrowser
import time

print("This program started on", time.ctime())
for i in range(3):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com")
