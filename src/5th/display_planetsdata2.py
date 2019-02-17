#!/usr/bin/env python

ff=open("planetsdata.dat", "r")
for item in ff.readlines():
    data=item.split()
    print data

ff.close()

