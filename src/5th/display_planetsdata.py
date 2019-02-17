#!/usr/bin/env python

ff=open("planetsdata.dat", "r")
for item in ff.readlines():
    print item[:-1]

ff.close()
