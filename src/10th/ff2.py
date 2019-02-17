#!/usr/bin/env python

from math import cos, sin, radians

g=9.80665

x=0.
y=0.

v0=float(raw_input("initial velocity in [m/s]? "))
theta=float(raw_input("Initial angle in [deg]? "))
n=float(raw_input("Number of steps? "))

t=0.
dt=10./n
vx=v0*cos(radians(theta))
vy=v0*sin(radians(theta))

ff=open("ff2_tmp.dat","w")

format = "%f\t%f\t%f\t%f\n"

for i in range(int(n)+1):
    ff.write(format % (t,x,y,vy))
    kx2 = dt * vx
    kvy1 = -g * dt
    ky2 = dt * (vy + kvy1/2.)
    kvy2 = -g*dt
    x += kx2
    y += ky2
    vy += kvy2

ff.close()
