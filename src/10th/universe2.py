#!/usr/bin/env python

from math import sqrt

h = 0.705
deltah = 0.013
Mpc = 3.0856776e19 #[km/Mpc]
tau = 365.256*24.*3600. * 10.**8. #[s/10^8yr]

ff = open("universe_tmp.dat","w")
format2 = "If omega0 = %f, the age of the universe Tuniv[10^8yr] in this model is\n %f <= Tuniv <= %f\n"
format4 = "If omega0 = %f, T(A=1) = %f\n"

Hmin = 100.*(h-deltah)
Hmax = 100.*(h+deltah)
tHmin = Mpc/Hmax/tau
tHmax = Mpc/Hmin/tau

format = "%13.11f\t%13.11f\n"
ome = float(raw_input("Omega0?: "))
n1 = raw_input("Number of steps1?: ")
n2 = raw_input("Number of steps2?: ")
tf = 8.
da = 1./float(n1)


#initial condition
t = 0. # T
a = 0. # A

ff.write(format % (t,a))

def fnc1(a):
    f = sqrt(a/(ome+(1.-ome)*a))
    return f
    
def fnc2(a):
    f = -ome/2./a**2.
    return f

for i in range (int(n1)):
    k2 = da*fnc1(a+da/2.)
    t += k2
    a += da
    ff.write(format % (t,a))
    
print format4 % (ome,t)
Tunivmin = t*tHmin
Tunivmax = t*tHmax
print format2 % (ome,Tunivmin,Tunivmax)

dt = (tf-t)/float(n2)
v = 1./fnc1(a)
for j in range (int(n2)):
    if a<=0.:
        break
    ka1 = dt*v
    kv1 = dt*fnc2(a)
    ka2 = dt*(v+kv1/2.)
    kv2 = dt*fnc2(a+ka1/2.)
    a += ka2
    v += kv2
    t += dt
    if a>=0.:
        ff.write(format % (t,a))
ff.close()
