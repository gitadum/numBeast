#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is made to train mental calculation skills
# ie addition (+), substraction (-), multiplication (*) and division (/)

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
