#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is made to train mental calculation skills
# ie addition (+), substraction (-), multiplication (*) and division (/)

import random
from functools import reduce
from datetime import datetime

def reckon(op, *terms):
    """
    The reckon function tests the user on one of the 4 basic operations
    for as many terms as there are following variables
    """
    try:
        assert len(terms) >= 2
    except AssertionError:
        raise TypeError("There should be at least 2 terms to do a calculation!")
    
    stt = 0
    opSig = ["+", "-", "*", "/"]
    opRes = [reduce(lambda t1,t2 : t1+t2, terms),
             reduce(lambda t1,t2 : t1-t2, terms),
             reduce(lambda t1,t2 : t1*t2, terms),
             reduce(lambda t1,t2 : t1/t2, terms)]

    sig = opSig[op]
    res = float(opRes[op])

    cal = f"{terms[0]}"
    for term in terms[1:]:
        cal += f" {sig} {term}"
    cal += " = "
    begin = datetime.now()
    ans = float(input(cal))
    if ans == res:
        stt += 1
    end = datetime.now()
    tim = end - begin
    return {
        'calcul': cal,
        'usrAns': ans,
        'corAns': res,
        'flagOK': stt,
        'timeSc': tim,
            }

def calculate(nTerms=(2,3), rangeTerm=(1,1000), operator="random"):
    """
    op : rank of the operation to be performed, a random number between 0 and 3
    0: addition, 1: substraction, 2: multiplication, 3: division"
    """
    terms = []
    for n in range(random.randint(*nTerms)):
        terms.append(random.randint(*rangeTerm))
    if operator == "random":
        op = random.randint(0,3)
    elif operator == "excludeDivision":
        op = random.randint(0,2)
    x = reckon(op, *terms)
    return x

def displayRes(x):
    print(x["calcul"])
    try:
        assert x['flagOK'] == 1
        print("Good answer.")
    except AssertionError:
        print("Bad answer.")
        print(f"You answered {x['usrAns']}")
        print(f"The answer was {x['corAns']}")
    finally:
        delta = str(x['timeSc']).replace(':','h',1).replace(':','m',1) + 's'
        print(f"Done within {delta}.")

def calculationSerie(n = 5):
    serie = []
    for i in range(5):
        calc = calculate(operator="excludeDivision")
        serie.append(calc)
    for calc in serie:
        displayRes(calc)
