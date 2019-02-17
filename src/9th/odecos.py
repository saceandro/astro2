#!/usr/bin/env python

from math import cos, pi

n = raw_input("Number of steps?: ")
u = 0.
t = 0.
dt = 2.*pi/float(n)

output = open("odecos_tmp.dat","w")

for i in range (int(n)+1):
    output.write(str(t)+"\t"+str(u)+"\n")
    u += dt *cos(t)
    t += dt

output.close()
