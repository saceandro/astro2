#!/usr/bin/env python

from math import exp

def f(x):
    a=exp(x)+1
    return a

def numresult(n):
    s=(f(0)+f(1))/2.
    for k in range (1,n):
        s=s+f(float(k)/float(n))
    t=s/float(n)               #number integral of the function f
    return t

N=raw_input("Accuracy N?: ")
print numresult(int(N))



        




    
    
