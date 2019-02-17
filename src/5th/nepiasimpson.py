#!/usr/bin/env python

from math import exp, fabs, e

def f(x):
    a = exp(x)+1
    return a

def numresult(n):
    s = f(0.)+f(1.)
    for k in range (1, n/2):
        u = 2.*float(k)/float(n)     # x_(2k)
        v = (2.*float(k)-1.)/float(n) # x_(2k-1)
        s = s + 2.*f(u) + 4.*f(v)
    w = 1. - 1./float(n)            # x_(n-1)
    s = s + 4.*f(w)
    t = s/3./float(n)   #number integral of the function f
    return t

N=raw_input("Accuracy N?: ")
print numresult(int(N))
