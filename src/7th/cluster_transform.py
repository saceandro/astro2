#!/usr/bin/env python

from math import log10

ff=open("cluster.dat", "r")
gg=open("tmp_cluster_transform.dat", "w")

format = "%f\t%f\n"

for item in ff.readlines():
    data = item.split()
    B = float(data[0])
    V = float(data[1])
    B_V = B - V
    gg.write(format % (B_V, V))

ff.close()
gg.close()
