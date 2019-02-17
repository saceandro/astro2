#!/usr/bin/env python

from math import log10, exp

epsilon = 7.1e-3    #energy transformation efficiency
q = 0.10            
X = 0.70            #rate of hydrogen
T0 = 365.256        #[day]   1[yr]=T0[day]
V = -26.75          #      visual apparent magnitude of the Sun
au = 1.4959787e11   #[m]
pc = 3.0856776e16   #[m]
Ms = 1.989e30       #[kg]  mass of the Sun
Ls = 3.839e26       #[W]   luminosity of the Sun
c = 2.99792458e8    #[m/s] velocity of light
Ma = 4.13           #      absolute magnitude

Mv = V - 5.*log10(au/10./pc) #(visual) absolute magnitude of the Sun

print Mv
