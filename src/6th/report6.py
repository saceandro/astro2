#!/usr/bin/env python

from math import pi, log10

au    = 1.4959787e11 #[m]
pc    = 2.06264806e5 #[AU]
L     = 3.839e26     #[W] :luminosity of the Sun
Rs    = 6.95508e8    #[m] :radius of the Sun
Rj    = 7.1492e7     #[m] :radius of Jupiter
Dj_s  = 5.2026       #[AU]:distance between Jupiter and the Sun
V     = -26.75       #    :visual apparent magnitude 
sigma = 5.670400e-8  #[W/m^2/K^4] :Stefan-Boltzmann constant

ff=open("tmp_report6.dat", "w")

def F(l,r):
    f=l/(4.*pi*r**2) # l[W], r[m]
    return f

#Question1
Fe_s = F(L,au)   #radiant flux of the Sun which the Earth receives
format1 = "Question1 \nRadiant flux of the Sun which the Earth receives \
is %-5.3e [W/m^2]\n\n"
ff.write(format1 % Fe_s)

#Question2
Te = (F(L,Rs)/sigma)**0.25  #effective temperature of the Sun's surface
format2 = "Question2 \nEffective temperature of the Sun's surface \
is %-5.3e [K]\n\n"
ff.write(format2 % Te)

#Question3
Mv = V - 5*log10(1./10./pc) #visual apparent magnitude of the Sun
format3 = "Question3 \nVisual apparent magnitude of the Sun is %-5.3e \n\n"
ff.write(format3 % Mv)

#Question4
Fj_s = F(L,Dj_s*au)     #radiant flux of the Sun which Jupiter receives [W/m^2]

Ej = pi * Rj**2. * Fj_s #energy Jupiter receives from the Sun [W]

De_j = Dj_s - 1.        #distance between the Earth and Jupiter [AU]

Fe_j = F(Ej,De_j*au)    #radiant flux of Jupiter which the Earth receives[W/m^2]

mj = V - 2.5*log10(Fe_j / Fe_s) #apparent magnitude of Jupiter

format4 = "Question4 \nApparent magnitude of Jupiter is %-5.3e"
ff.write(format4 % mj)

ff.close()

