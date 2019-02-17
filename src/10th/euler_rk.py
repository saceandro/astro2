#!/usr/bin/env python

from math import e, fabs

def numresult(n):
    t=0.
    u=1.
    dt=1./float(n)
    for i in range (int(n)):
        k1 = dt*u
        k2 = dt*(u + k1/2.)
        u += k2
    return u

ff=open("euler_rk_tmp.dat","w")

format = "%d\t%13.11e\n"

for j in (1,10,100,1000,10000):
    error = fabs(numresult(j)/e -1.)
    ff.write(format % (j,error))

ff.close()
        
