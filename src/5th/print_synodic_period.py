#!/usr/bin/env python

from math import fabs

planet=[]
sidereal_period=[]

ff=open("planets.dat", "r")
for item in ff.readlines():
    data=item.split()
    planet.append(data[0])
    sidereal_period.append(data[2])
ff.close()

format="The synodic period between %s and %s is %-7.5f [yr]"

gg=open("tmp_print_synodic_period.dat", "w")
for i in range(8):
    p1=sidereal_period[i]
    for j in range (i+1,8):
        p2=sidereal_period[j]
        synodic_period=fabs(1./((1./float(p1))-(1./float(p2))))
        gg.write(format % (planet[i], planet[j], synodic_period) + "\n")
gg.close()
