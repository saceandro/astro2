#!/usr/bin/env python

from math import pi

hh=open("tmp_avgdensity.dat", "w")
hh.close()

ff=open("planetsdata.dat", "r")
for item in ff.readlines():
    data=item.split()
    R=float(data[1])*10**5
    M=float(data[2])*10**3
    d=3.*M/4./pi/R**3.

    gg=open("tmp_avgdensity.dat", "a")
    format="Average density of %s is %5.2f [g*cm**(-3)]\n"
    aa=format % (data[0], d)
    gg.write(aa)
    gg.close()

