#!/usr/bin/env python

from math import pi, degrees

T=float(raw_input("Time evolution?: "))
dt = 0.001
N = int(T/dt)

a = 0.8
e = 0.8

#initial condition
r = 1.
theta = 0.
v = 0.
ome = 1.25

ff = open("report10_tmp.dat","w")
format = "%13.11f\t%13.11f\t%13.11f\n"
format2 ="%13.11f"

def f1(r,ome):
    f = r * ome**2. -1./r**2. - 3. * e**2. * a**2./10./r**4.
    return f

def f2(r,v,ome):
    f = -2.*v*ome/r
    return f

v_n = []
theta_n = []

for i in range (N+1):
    v_n.append(v)
    theta_n.append(theta)
    ff.write(format % (theta,v,r))
    kr1 = dt*v
    kv1 = dt*f1(r,ome)
    ktheta1 = dt*ome
    kome1 = dt*f2(r,v,ome)
    kr2 = dt*(v+kv1/2.)
    kv2 = dt*f1(r+kr1/2.,ome+kome1/2.)
    ktheta2 = dt*(ome+kome1/2.)
    kome2 = dt*f2(r+kr1/2.,v+kv1/2.,ome+kome1/2.)
    r += kr2
    v += kv2
    theta += ktheta2
    ome += kome2
    
ff.close()
for j in range (1,N):
    if v_n[j]<=0. and v_n[j+1]>=0.:
        Alpha = theta_n[j]\
                - v_n[j]*(theta_n[j+1]-theta_n[j])/(v_n[j+1]-v_n[j])
        print format2 % Alpha

