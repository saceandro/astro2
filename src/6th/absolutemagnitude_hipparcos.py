#!/usr/bin/env python

from math import log10

V=[]
P=[]
B_V=[]

ff=open("hipparcos.dat", "r")
for item in ff.readlines():
    V.append(item[41:46])
    P.append(item[79:86])
    B_V.append(item[245:251])
ff.close()

format ="%f \t %f \n"

gg=open("tmp_absolutemagnitude_hipparcos.dat", "w")
for i in range (len(V)):
    p = float(P[i])
    v = float(V[i])
    b_v = float(B_V[i])
    Mv = v + 5.*log10(p) -10.   #visual absolute magnitude
    aa = format % (b_v, Mv)
    gg.write(aa)
gg.close()

