#!/usr/bin/env python

radius={}
ff=open("planetsdata.dat", "r")
for item in ff.readlines():
    data=item.split()
    radius[data[0]]=data[1]
    
print radius
ff.close()
