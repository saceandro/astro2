#!/usr/bin/env python

from math import pi, cos, sin, radians

h = 0.705

format = "%f\t%f\n"
ff=open("zcat.dat", "r")
gg=open("zcat_trans_tmp.dat", "w")

for item in ff.readlines():
    v=item[31:36] #[km/s]
    if v != "     ":
        f=float(item[11:13]) 
        g=float(item[13:15])
        l=float(item[15:19])
        
        m=float(item[19:22])
        n=float(item[22:24])
        
        a = f + g/60. +l/3600. #[ji]
        b = m + n/60.          #[deg]
        
        if a>=8. and a<=17. and b>=25. and b<=35. and float(v)<=15000.:
            alpha = (2.*pi/24.)*a   #[rad]
            delta = radians(b)      #[rad]
            d = float(v)/(100.*h)   #[Mpc]
            ds = d*cos(delta)
            x = ds*cos(alpha)
            y = ds*sin(alpha)
            gg.write(format % (x, y))

ff.close()
gg.close()
            
            

            

            
        

        
        
        
        

    
    
