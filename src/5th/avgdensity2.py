#!/usr/bin/env python

from math import pi

format="Average density of %s is %5.2f [g*cm**(-3)]\n"
ff=open("planetsdata.dat", "r")
gg=open("tmp_avgdensity2.dat", "w")

for item in ff.readlines():
    data=item.split()
    R=float(data[1])*10**5
    M=float(data[2])*10**3
    d=3.*M/4./pi/R**3.
    gg.write(format % (data[0], d))
ff.close()
gg.close()
