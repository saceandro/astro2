#!/usr/bin/env python

from math import sqrt

h = 0.705
deltah = 0.013
Mpc = 3.0856776e19 #[km/Mpc]
tau = 365.256*24.*3600. * 10.**8. #[s/10^8yr]

format = "%13.11f\t%13.11f\n"
format2 = "If omega0 = %3.1f, the age of the universe Tuniv[10^8yr] in this model is\n %f <= Tuniv <= %f\n\n"
format3 = "Hubble time tH[10^8yr] is %f <= tH <= %f\n\n"
format4 = "If omega0 = %3.1f, T(A=1) = %f\n"

gg = open("universe_age.dat","w")

Hmin = 100.*(h-deltah)
Hmax = 100.*(h+deltah)
tHmin = Mpc/Hmax/tau
tHmax = Mpc/Hmin/tau
gg.write(format3 % (tHmin,tHmax))

n1 = raw_input("Number of steps1?: ")
n2 = raw_input("Number of steps2?: ")
tf = 3.
da = 1./float(n1)

def openfile(i):
    if i==0.5:
        return open("universe0point5.dat","w")
    elif i==1.:
        return open("universe1.dat","w")
    elif i==2.:
        return open("universe2.dat","w")

for ome in (0.5,1.,2.):
    def fnc1(a):
        f = sqrt(a/(ome+(1.-ome)*a))
        return f
    
    def fnc2(a):
        f = -ome/2./a**2.
        return f
    
    t = 0. # initial T
    a = 0. # initial A
    ff = openfile(ome)
    ff.write(format % (t,a))
    for i in range (int(n1)):
        k2 = da*fnc1(a+da/2.)
        t += k2
        a += da
        ff.write(format % (t,a))
        
    gg.write(format4 % (ome,t))
    Tunivmin = t*tHmin
    Tunivmax = t*tHmax
    gg.write(format2 % (ome,Tunivmin,Tunivmax))
    
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
gg.close()
        
                
        
    
