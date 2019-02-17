#!/usr/bin/env python

from math import log10

ff=open("ngc188.dat", "r")
gg=open("tmp_ngc188_transform.dat", "w")

for item in ff.readlines():
    data = item.split()
    B = float(data[0])
    V = float(data[1])
    B_V = B - V
    Mv = V - 5.*log10(1.6e3 / 10)
    format = "%f \t %f\n"
    gg.write(format % (B_V, Mv))

ff.close()
gg.close()

    
