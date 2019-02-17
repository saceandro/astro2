#!/usr/bin/env python

periodEarth = 1.00004 # Earth's sidereal period in [yr]
periodMercury = 0.24085 # Mercury's sidereal period in [yr]
periodVenus = 0.61521 # Venus' sidereal period in [yr]

planet=raw_input("Which planet?: ")
format="The synodic period between Earth and %s is %-7.5f [yr]"

if planet =="Mercury":
    synodic=1. /((1./periodMercury)-(1./periodEarth))
    print format % (planet,synodic)
elif planet =="Venus":
    synodic=1. /((1./periodVenus)-(1./periodEarth))
    print format % (planet,synodic)
else:
    print "%s is not an inferior planet!" % planet

    
