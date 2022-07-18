import random
from main import reckon

t1 = random.randint(1,1000) # First term, random integer between 1 and 1,000
t2 = random.randint(1,1000) # Second term, random integer between 1 and 1,000
op = random.randint(0,3) # rank of the operation to be performed
                         # a random number between 0 and 3
                         # 0: addition, 1: substraction,
                         # 2: multiplication, 3: division

x = reckon(t1,t2,op)

try:
    assert x['flagOK'] == 1
    print("Good answer.")
except AssertionError:
    print("Bad answer.")
    print(f"The answer was {x['corAns']}")
finally:
    delta = str(x['timeSc']).replace(':','h',1).replace(':','m',1) + 's'
    print(f"Done within {delta}.")