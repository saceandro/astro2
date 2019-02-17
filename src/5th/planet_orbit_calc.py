#!/usr/bin/env python

from math import pi, cos

a=[]          #Semimajor axis in [AU]
ec=[]         #Eccentricity

ff=open("planet_orbit.dat", "r")
for item in ff.readlines():
    data=item.split()
    a.append(data[1])
    ec.append(data[2])
ff.close()

def r(t, a, ec):
    l=a*(1-ec**2)/(1+ec*cos(t))
    return l

format1="%10.6f[rad]\t"
format2="%10.6f[AU]\t"

gg=open("tmp_planet_orbit_calc.dat", "w")
t=0.
for i in range (201):
    t=i*0.01*pi
    gg.write(format1 % t)
    for j in range (4):
        R=r(t, float(a[j]), float(ec[j]))
        gg.write(format2 % R)
    gg.write("\n")
gg.close()
        
        
        
    




        
    
    
    
    


    
    
    

