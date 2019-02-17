#!/usr/bin/env python

from math import exp, fabs, e

def f(x):
    a=exp(x)+1
    return a

def numresult(n):
    s=(f(0)+f(1))/2.
    for k in range (1,n):
        s=s+f(float(k)/float(n))
    t=s/float(n)               #number integral of the function f
    return t

format="%d \t %13.11e \n"

ff=open("tmp_nepia.dat", "w")
for n in (5,10,20,50,100,200,500,1000,2000,5000,10000):
    error=fabs(numresult(n)/e - 1.)
    ff.write(format % (n, error))
ff.close()
        
        
            

