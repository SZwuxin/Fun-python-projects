import random
import time


def deepCave(width, emptySpaceCount):
    while True:
        if emptySpaceCount >= width:
            print(' '*emptySpaceCount)
        else:
            r = random.randint(1, width-emptySpaceCount)
            print('#'*r + ' '*emptySpaceCount + '#'*(width-emptySpaceCount-r))
        time.sleep(0.2)

width = input('Input the width of the deepCave')
emptySpaceCount = input('Enter the amount of empty space in regard to the width')
try:
    deepCave(int(width), int(emptySpaceCount))
except Exception:
    print('Invalid input')