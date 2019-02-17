#!/usr/bin/env python

from math import fabs

sidereal_period={}
ff=open("planets.dat", "r")
for item in ff.readlines():
    data=item.split()
    sidereal_period[data[0]]=data[2]
ff.close()

planet1=raw_input("Which planet does the observer stands?: ")
planet2=raw_input("Which planet does the observer observes?: ")
format="The synodic period between %s and %s is %-7.5f [yr]"

p1=sidereal_period[planet1]
p2=sidereal_period[planet2]

synodic_period=fabs(1./((1./float(p1))-(1./float(p2))))

print format % (planet1, planet2, synodic_period)




    
