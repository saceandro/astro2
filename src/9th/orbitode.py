#!/usr/bin/env python

ff=open("orbitode_tmp.dat","w")

format = "%f\t%f\n"

ti=0.
tf=float(raw_input("Time evolution?: "))
n = raw_input("Number of steps?: ")
dt= (tf-ti)/float(n)

#initial condition
t=ti
r=1.
theta=0.
vr=0.
ome=1.2

for i in range (int(n)+1):
    ff.write(format % (theta,r))
    r1 = r + dt*vr
    vr1 = vr + dt*(r*ome**2. - 1./r**2.)
    theta1 = theta + dt*ome
    ome1 = ome - dt*2.*vr*ome/r
    
    r=r1
    vr=vr1
    theta=theta1
    ome=ome1

ff.close()

    
    
