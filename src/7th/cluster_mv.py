#!/usr/bin/env python

from math import log10

d = 136.3  #distance between the cluster and the Earth

ff=open("cluster.dat", "r")
gg=open("cluster_mv_tmp.dat", "w")

format = "%f\t%f\n"

for item in ff.readlines():
    data = item.split()
    B = float(data[0])
    V = float(data[1])
    B_V = B-V
    Mv = V - 5.*log10(d/10.)
    gg.write(format % (B_V,Mv))

ff.close()
gg.close()

    
    
    
