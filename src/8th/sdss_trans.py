#!/usr/bin/env python

from math import pi, cos, sin, radians

h = 0.705

format = "%f\t%f\n"
ff=open("sdss.dat", "r")
gg=open("sdss_trans_tmp.dat", "w")

for item in ff.readlines():
    alpha = radians(float(item[10:20])) #[rad]
    delta = radians(float(item[20:35])) #[rad]
    v = float(item[0:10])      #[km/s]
    if v <= 80000.:
        vs = v*cos(delta)
        x = vs*cos(alpha)
        y = vs*sin(alpha)
        gg.write(format % (x, y))

ff.close()
gg.close()
