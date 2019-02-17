#!/usr/bin/env python

from math import cos,sin,sqrt,radians

ff=open("sb_tmp.dat","w")

format = "%13.11e\t%13.11e\t%13.11e\t%13.11e\t%13.11e\t%13.11e\n"

tf=1.4
dt=1.00e-5
n=int(tf/dt)

q = 0.012300
Re = 6.378e6 #[m]
Rm = 1.738e6 #[m]
d = 3.844e8 #[m]

re = Re/d
rm = Rm/d

#initial condition
t=0.
x=re
y=0.
v=10.91
a=20.
vx=v*cos(radians(a))
vy=v*sin(radians(a))

def X(t):
    X=cos(t)
    return X

def Y(t):    
    Y=sin(t)
    return Y

def r(x,y):
    r = sqrt(x**2. + y**2.)
    return r

def R(t,x,y):
    R = sqrt((X(t)-x)**2. + (Y(t)-y)**2.)
    return R
    
def f1(t,x,y):
    f = -x/r(x,y)**3. + q*(X(t)-x)/R(t,x,y)**3.
    return f

def f2(t,x,y):
    g = -y/r(x,y)**3. + q*(Y(t)-y)/R(t,x,y)**3.
    return g

def f3(t,x,y,vx,vy):
    h = (vx**2. +vy**2.)/2. - 1./r(x,y) - q/R(t,x,y)
    return h

print f3(t,x,y,vx,vy)
    
for i in range (int(n)+1):
    if r(x,y)<re:
        print "r<re !"
        break
    
    elif R(t,x,y)<rm:
        print "R<rm !"
        break
    
    E = f3(t,x,y,vx,vy)
    ff.write(format % (t,x,y,X(t),Y(t),E))
    
    kx1 = dt*vx
    ky1 = dt*vy
    kvx1 = dt*f1(t,x,y)
    kvy1 = dt*f2(t,x,y)
    kx2 = dt*(vx + kvx1/2.)
    ky2 = dt*(vy + kvy1/2.)
    kvx2 = dt*f1(t+dt/2.,x+kx1/2.,y+ky1/2.)
    kvy2 = dt*f2(t+dt/2.,x+kx1/2.,y+ky1/2.)

    t += dt
    x += kx2
    y += ky2
    vx += kvx2
    vy += kvy2

ff.close()
print E


    



    
    

    
    

