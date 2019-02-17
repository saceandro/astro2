#!/usr/bin/env python

from math import e, fabs

def error(n):
    t=0.
    u=1.
    dt=1./float(n)
    for i in range (int(n)):
        t += dt
        u += u*dt
    er = fabs(u/e - 1.)
    print n, er

for n in (1,10,100,1000,10000):
    error(n)

