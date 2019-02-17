#!/usr/bin/env python

from math import cos, pi

n = 100
u = 0.
t = 0.
dt = 2.*pi/float(n)

ff = open("sample2.dat","w")

format = "%13.11f\t%13.11f\n"

for i in range (int(n)+1):
    ff.write(format % (t,u))
    k2 = dt * cos(t+dt/2.)
    u += k2
    t +=dt

ff.close()


