#!/usr/bin/env python

from math import fabs, log10

error={}
ff=open("tmp_nepia.dat", "r")
for item in ff.readlines():
    data=item.split()
    error[data[0]]=data[1]
ff.close()

gradient=fabs((log10(float(error[str(100)]))-log10(float(error[str(10000)])))/(log10(100.)-log10(10000.)))

print gradient


