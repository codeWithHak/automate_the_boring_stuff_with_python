# two ways of importing modules
# import random   --- you have tou use the prefixe random. before accessing any method from this module ---
from random import *  # --- you use any method from random directly without the prefix random. ---
import sys

# this function will print 5 random integers
# for i in range(5):
#   print(random.randint(1,10)) #- with first import
#   print(randint(1,10)) #- with second import


# sys.exit() to exit any program in between the floww
while True:
    command  = input("type exit ")
    if command == "exit":
        print("exitting")
        break
    print("Yout typed", command)