#!/usr/bin/env python

from math import e, fabs

def numresult(n):
    t=0.
    u=1.
    dt=1./float(n)
    for i in range (int(n)):
        u += u*dt
    return u

ff=open("euler_tmp.dat","w")

format = "%d\t%13.11e\n"

for j in (1,10,100,1000,10000):
    error = fabs(numresult(j)/e -1.)
    ff.write(format % (j,error))

ff.close()
