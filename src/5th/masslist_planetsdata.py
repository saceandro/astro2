#!/usr/bin/env python

mass=[]
ff=open("planetsdata.dat", "r")
for item in ff.readlines():
    data=item.split()
    mass.append(data[2])
    
print mass
ff.close()
