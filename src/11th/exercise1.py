#!/usr/bin/env python

from math import sqrt,e,log

omem0 = 0.00001
omela0 = 0.99999

format = "%13.11e\t%13.11e\t%13.11e\t%13.11e\n"

n1 = raw_input("Number of steps1?: ")
n2 = raw_input("Number of steps2?: ")
tf = 10.
da = 1./float(n1)

def fnc1(a):
    f = sqrt(a/(omem0 + omela0 * a**3.))
    return f
    
def fnc2(a):
    f = -omem0/2./a**2. + omela0*a
    return f
    
t = 0. # initial T
a = 0. # initial A

T = []
Omem = []
gg = open("omega2.dat","w")

for i in range (int(n1)):
    k2 = da*fnc1(a+da/2.)
    t += k2
    a += da
    omela = omela0 * (a * fnc1(a))**2.
    omem = omem0 * fnc1(a)**2./a
    gg.write(format % (t,a,omem,omela))
    T.append(t)
    Omem.append(omem)
    
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
        omela = omela0 * (a/v)**2.
        omem = omem0/a/v**2.
        gg.write(format % (t,a,omem,omela))
        T.append(t)
        Omem.append(omem)
gg.close()

grad = (log(Omem[60000],e)-log(Omem[100000],e))/(T[60000]-T[100000])
print grad
print T[60000],Omem[60000]
print T[100000],Omem[100000]
