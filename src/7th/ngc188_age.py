#!/usr/bin/env python

from math import log10

epsilon = 7.1e-3    #energy transformation efficiency
q = 0.10            #rate of burning hydrogen 
X = 0.70            #rate of hydrogen among whole mass
T0 = 365.256        #[day]   1[yr]=T0[day]
V = -26.75          #visual apparent magnitude of the Sun
au = 1.4959787e11   #[m]
pc = 3.0856776e16   #[m]
Ms = 1.989e30       #[kg]  mass of the Sun
Ls = 3.839e26       #[W]   luminosity of the Sun
c = 2.99792458e8    #[m/s] velocity of light
Ma = 4.13           #absolute magnitude of the star among NGC 188 which is
#                    about to leave main sequence

Mv = V - 5.*log10(au/10./pc) #(visual) absolute magnitude of the Sun

T=T0 * 24. * 3600. * 10**8.  # 1[10^8 yr]=T[sec]

tau = (epsilon* q* X* Ms* c**2./Ls/T)* 10.**((Ma-Mv)/3.5) #age of NGC 188
#                                                          [10^8 yr]

format = "%-3.1e [10^8 yr]"

print format % tau 
