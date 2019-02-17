#!/usr/bin/env python

pi=3.1416 
G=6.67428e-11 # Gravitational constant in [m**3/kg/s**2]
M=1.899e27 # Jupiter mass in [kg]

a=raw_input("Semimajor axis [m]?: ")
format="Period of the satellite is %5.2f [days]"

period=(4*(pi**2)*(float(a)**3)/((24*3600)**2)/G/M)**0.5
print format % period

