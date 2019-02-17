#!/usr/bin/env python

from math import log10

V=[]    #visual apparent magnitude
P=[]    #annual parallax [parallax millisecond]
B_V=[]  #B-V

ff=open("wellknownstars.dat", "r")
for item in ff.readlines():
    data=item.split()
    V.append(data[1])
    P.append(data[2])
    B_V.append(data[3])
ff.close()

format="%f \t %f \n"

gg=open("tmp_absolutemagnitude.dat", "w")
for i in range(7):
    p = float(P[i])
    v = float(V[i])
    b_v = float(B_V[i])
    Mv = v + 5.*log10(p) -10.   #visual absolute magnitude
    aa = format % (b_v, Mv)
    gg.write(aa)
gg.close()
    
    
