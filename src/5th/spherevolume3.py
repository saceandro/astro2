#!/usr/bin/env python

from math import pi, pow

coef = 4.*pi/3.

def func(radius, a=coef):
    volume = a*pow(radius, 3.)
    print "the volume is ", volume

rad=raw_input("Radius?: ")
func(float(rad))
func(float(rad), 1.)
