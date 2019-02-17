#!/usr/bin/env python

from math import pi, log10

au    = 1.4959787e11 #[m]
pc    = 2.06264806e5 #[AU]
L     = 3.839e26     #[W] :luminosity of the Sun
Rs    = 6.95508e8    #[m] :radius of the Sun
Rj    = 7.1492e7     #[m] :radius of Jupiter
Dj_s  = 5.2026       #[AU]:distance between Jupiter and the Sun
V     = -26.75       #    :visual apparent magnitude 
sigma = 5.670400e-8  #[W/m^2/K^4]

Fe_jwaruFe_s = (Rj/2./au/Dj_s/(Dj_s -1.))**2

mj = V - 2.5*log10(Fe_jwaruFe_s)

print mj
