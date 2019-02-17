#!/usr/bin/env python

from math import e, fabs, log10

def error(n):
    t=0.
    u=1.
    dt=1./float(n)
    for i in range (int(n)):
        k1 = dt*u
        k2 = dt*(u + k1/2.)
        u += k2
    logerror = log10(fabs(u/e -1.))
    return logerror

grad = (error(10000)-error(10))/(4.-1.)

print grad
