#!/usr/bin/env python

from math import fabs, log10

error={}
ff=open("tmp_simpsonrule.dat", "r")
for item in ff.readlines():
    data=item.split()
    error[data[0]]=data[1]
ff.close()

gradient=fabs((log10(float(error[str(8)]))-log10(float(error[str(500)])))/(log10(8)-log10(500)))

print gradient
