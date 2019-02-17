#!/usr/bin/env python

from math import pi

ff=open("2bprob_tmp.dat","w")

format = "%f\t%f\t%f\t%f\n"

ti=0.
tf=float(raw_input("Time evolution until?: "))
n = raw_input("Number of steps?: ")
dt= (tf-ti)/float(n)

#initial condition
r1i = 2.
r2i = 1.
theta1i = 0.
theta2i = pi
vr1i = 0.
vr2i = 0.
ome1i = 0.1
ome2i = 0.1

for i in range (int(n)+1):
    ff.write(format % (theta1i,r1i,theta2i,r2i))
    r1f = r1i + dt*vr1i
    vr1f = vr1i + dt*(r1i * ome1i**2. - (2./3.) / (r1i + r2i)**2.)
    theta1f = theta1i + dt*ome1i
    ome1f = ome1i - dt*2.*vr1i*ome1i/r1i
    r2f = r2i + dt*vr2i
    vr2f = vr2i + dt*(r2i * ome2i**2. - (1./3.) / (r1i + r2i)**2.)
    theta2f = theta2i + dt*ome2i
    ome2f = ome2i - dt*2.*vr2i*ome2i/r2i

    r1i = r1f
    r2i = r2f
    theta1i = theta1f
    theta2i = theta2f
    vr1i = vr1f
    vr2i = vr2f
    ome1i = ome1f
    ome2i = ome2f

ff.close()

    
    
    

    

