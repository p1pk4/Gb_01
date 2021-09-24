import time
import sys

for i in "7 6 5 4 3 2 1":
    time.sleep(0.5)
    sys.stdout.write(i)
    sys.stdout.flush()