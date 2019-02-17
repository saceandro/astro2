#!/usr/bin/env python

from math import pi

ff=open("2bprob_tmp.dat","w")

format = "%f\t%f\t%f\t%f\n"

ti=0.
tf=float(raw_input("Time evolution until?: "))
n = raw_input("Number of steps?: ")
dt= (tf-ti)/float(n)

yi = {}
yf = {}

#initial condition
yi[(1,1)]=2.
yi[(2,1)]=1.
yi[(1,2)]=0.
yi[(2,2)]=pi
yi[(1,3)]=0.
yi[(2,3)]=0.
yi[(1,4)]=0.1
yi[(2,4)]=0.1

delta = {}
delta[1]=2.
delta[2]=1.

def fnc(k,l):
    if l==1:
        a=yi[(k,2)]
    elif l==2:
        a=yi[(k,1)] * yi[(k,4)]**2.\
           -delta[k]/3./(yi[(1,1)]+yi[(2,1)])**2.
    elif l==3:
        a= yi[(k,4)]
    elif l==4:
        a=-2.*yi[(k,2)]*yi[(k,4)]/yi[(k,1)]
    return a

for j in range (int(n)+1):
    ff.write(format % (yi[(1,2)],yi[(1,1)],yi[(2,2)],yi[(2,1)]))
    for m in (1,2):
        for o in range (1,5):
            yf[(m,o)] = yi[(m,o)] + dt*fnc(m,o)
            
    for m in (1,2):
        for o in range (1,5):
            yi[(m,o)] = yf[(m,o)]

ff.close()
        
        
        
             
    
