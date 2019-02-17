#!/usr/bin/env python

from math import e, fabs, log10

def numresult(n):
    t=0.
    u=1.
    dt=1./float(n)
    for i in range (int(n)):
        u += u*dt
    return u

def error(j):
    er = fabs(numresult(j)/e -1.)
    return er

grad = (log10(error(10))-log10(error(10000)))/(1.-4.)

print grad
