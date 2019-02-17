#!/usr/bin/env python

from math import pi, pow

def func(radius):
    volume=4.*pi*pow(radius, 3.)/3.
    return volume

rad=raw_input("Radius?: ")
print "The volume is ", func(float(rad))
