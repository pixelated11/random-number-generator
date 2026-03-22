import random
import time
import os

print("Random number generator, by pixelated.")
time.sleep(2)

def mainProgram():
    x = int(input("Type in the starting range:"))
    y = int(input("Type in the end range:"))
    time.sleep(1)
    print("Random number is")
    print(random.randrange(x, y))

mainProgram()
os.system("pause")