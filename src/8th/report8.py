#!/usr/bin/env python

from math import pi, log

T0=365.256 #[day/yr]
pc=3.0856776e16 #[m/pc]=[km/kpc]
G=6.67428e-11 #[m^3/kg/s^2]
v=220. #[km/s] :velocity of the sun
r=8. #[kpc] :distance between the center of the galactic system and the sun
Ms=1.9891e30 #[kg] :mass of the sun
ts=50. #[10^8yr] :age of the sun
mall = 5.4e11 # mall*Ms = "Whole mass of the galactic system"

ff=open("report8_tmp.dat", "w")

#Question1
T1 = T0 * 24. * 3600. * 10.**8. #[s/10^8yr]
P = 2.*pi*r*pc/v #[s]
P0 = P/T1 #[10^8yr]
format1 = "Question1\n %-3.1e [10^8yr]\n\n"
ff.write(format1 % (P0))

#Question2
N = ts/P0
format2 ="Question2\n %-3.1e\n\n"
ff.write(format2 % (N))

#Question3
R = r*pc *10.**3. #[m]
V = v * 10.**3.   #[m/s]
m = (R * V**2.) / (G * Ms)
format3 = "Question3\n %-3.1e\n\n"
ff.write(format3 % (m))

#Question4
alpha = log((m/mall),(8./50.))
format4 = "Question4\n %-3.2e\n\n"
ff.write(format4 % alpha)

ff.close()
