#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is made to train mental calculation skills
# This version of the program involves 2 terms and one of the 4 basic operations
# ie addition (+), substraction (-), multiplication (*) and division (/)

import random
#import time
from timer import timer

t1 = random.randint(1,1000) # First term, random integer between 1 and 1,000
t2 = random.randint(1,1000) # Second term, random integer between 1 and 1,000
op = random.randint(0,3) # rank of the operation to be performed
                         # a random number between 0 and 3
                         # 0: addition, 1: substraction,
                         # 2: multiplication, 3: division

@timer
def reckon(t1, t2, op):
    opSig = ["+", "-", "*", "/"]
    opRes = [t1+t2, t1-t2, t1*t2, t1/t2]

    sig = opSig[op]
    res = float(opRes[op])

#    begin = time.time()
    ans = float(input(f"{t1} {sig} {t2} = "))
    try:
        assert ans == res
        print("Good answer.")
    except AssertionError:
        print("Bad answer.")
        print(f"The answer was: {res}")
#    end = time.time()

#    print("Done in {d} s.".format(d=(end-begin)))
if __name__ == "__main__":
    reckon(t1,t2,op)