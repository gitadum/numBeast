import random
from main import reckon as reckonv2

t1 = random.randint(1,1000) # First term, random integer between 1 and 1,000
t2 = random.randint(1,1000) # Second term, random integer between 1 and 1,000
op = random.randint(0,3) # rank of the operation to be performed
                         # a random number between 0 and 3
                         # 0: addition, 1: substraction,
                         # 2: multiplication, 3: division

def calculate(nTerms=random.randint(2,3), rangeTerms=random.randint(1,1000),
              operator="random"):
    terms = []
    for n in range(nTerms):
        terms.append(rangeTerms)
    print(terms)
    if operator == "random":
        op = random.randint(0,3)
    elif operator == "excludeDivision":
        op = random.randint(0,2)
    x = reckonv2(op, *terms)
    try:
        assert x['flagOK'] == 1
        print("Good answer.")
    except AssertionError:
        print("Bad answer.")
        print(f"The answer was {x['corAns']}")
    finally:
        delta = str(x['timeSc']).replace(':','h',1).replace(':','m',1) + 's'
        print(f"Done within {delta}.")

calculate(operator="excludeDivision")