#!/usr/bin/env python

ff=open("gensui_tmp.dat","w")

from math import sqrt

format = "%13.11f\t%13.11f\t%13.11f\n"

ome = sqrt(10.)
lamda = 1.

n = 10000
dt = 10./float(n)

#initial condition
t = 0.
x = 0.
v = 1.

for i in range (int(n)+1):
    ff.write(format % (t,x,v))
    t += dt
    x1 = x + dt*v
    v1 = v + dt*(-ome**2. * x - 2.*lamda*v)
    
    x=x1
    v=v1

ff.close()
