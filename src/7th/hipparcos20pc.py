#!/usr/bin/env python

from math import log10

ff=open("../6th/hipparcos.dat", "r")
gg=open("tmp_hipparcos20pc.dat", "w")

format ="%f\t%f\n"

for item in ff.readlines():
    p=float(item[79:86])        #annual parallax [millisecond degree]
    d = 10.**3./p               #distance: d[pc]
    if  d<=20.:
        v=float(item[41:46])        #visual apparent magnitude
        b_v=float(item[245:251])    #B-V
        Mv = v + 5.*log10(p) -10.   #visual absolute magnitude
        aa = format % (b_v, Mv)
        gg.write(aa)
    
ff.close()
gg.close()
