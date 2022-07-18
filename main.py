#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# This program is made to train mental calculation skills
# This version of the program involves 2 terms and one of the 4 basic operations
# ie addition (+), substraction (-), multiplication (*) and division (/)

from datetime import datetime

def reckon(t1, t2, op):
    stt = 0
    opSig = ["+", "-", "*", "/"]
    opRes = [t1+t2, t1-t2, t1*t2, t1/t2]

    sig = opSig[op]
    res = float(opRes[op])

    cal = f"{t1} {sig} {t2} = "
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
