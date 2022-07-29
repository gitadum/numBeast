#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is made to train mental calculation skills
# ie addition (+), substraction (-), multiplication (*) and division (/)

import random
from functools import reduce
from datetime import datetime
from timer import timer


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


def selectRandomInt(lowBound=0, upBound=3, exclude=None):
    while True:
        y = random.randint(lowBound, upBound)
        try:
            assert type(exclude) != list
            if y != exclude: break
        except AssertionError:
            if y not in exclude: break
    return y


def calculate(nTerms=(2,3), rangeTerm=(1,1000), operator="random"):
    """
    op : rank of the operation to be performed, a random number between 0 and 3
    0: addition, 1: substraction, 2: multiplication, 3: division"
    """
    terms = []
    for n in range(selectRandomInt(*nTerms)):
        terms.append(selectRandomInt(*rangeTerm))
    if operator == "random":
        op = selectRandomInt()
    elif operator == "excludeMultiplication":
        op = selectRandomInt(exclude=2)
    elif operator == "onlyMultiplication":
        op = 2
    elif operator == "excludeDivision":
        op = selectRandomInt(exclude=3)
    elif operator == "onlyDivision":
        op = 3
    x = reckon(op, *terms)
    return x


def displayRes(x):
    msg = ""
    try:
        assert x['flagOK'] == 1
        msg += x["calcul"] + f"{x['usrAns']}"
        msg += " " + "Good answer."
    except AssertionError:
        msg += x["calcul"].replace(" = ", "") + " =/= " + f"{x['usrAns']}"
        msg += " " + "Bad answer."
        msg += " " + f"The answer was {x['corAns']}."
    finally:
        delta = str(x['timeSc']).replace(':','h',1).replace(':','m',1) + 's'
        msg += " " + f"Done within {delta}."
        print(msg)


@timer
def calculationSerie(n = 5, *args, **kwargs):
    decorLine = 8 * "-"
    serie = []
    for i in range(n):
        calc = calculate(*args, **kwargs)
        serie.append(calc)
    print(decorLine)
    for calc in serie:
        displayRes(calc)
    print(decorLine)


def multiplicationTables(n=10, multipleRange=(1,12)):
    calculationSerie(n=n, nTerms=(2,2), rangeTerm=multipleRange, 
                     operator="onlyMultiplication")
