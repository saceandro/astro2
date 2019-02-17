#!/usr/bin/env python

periodEarth=1.00004 # Earth's sidereal period in [yr]
periodMars=1.88089 # Mars' sidereal period in [yr]
periodJupiter=11.8622 # Jupiter's sidereal period in [yr]
periodSaturn=29.4578 # Saturn's sidereal period in [yr]
periodUranus=84.0223 # Uranus' sidereal period in [yr]
periodNeptune=164.774 # Neptune's sidereal period in [yr]

planet=raw_input("Which planet?: ")
format="The synodic period between Earth and %s is %-7.5f [yr]"

if planet=="Mars":
    synodic=1./((1./periodEarth)-(1./periodMars))
    print format % (planet, synodic)
elif planet=="Jupiter":
    synodic=1./((1./periodEarth)-(1./periodJupiter))
    print format % (planet, synodic)
elif planet=="Saturn":
    synodic=1./((1./periodEarth)-(1./periodSaturn))
    print format % (planet, synodic)
elif planet=="Uranus":
    synodic=1./((1./periodEarth)-(1./periodUranus))
    print format % (planet, synodic)
elif planet=="Neptune":
    synodic=1./((1./periodEarth)-(1./periodNeptune))
    print format % (planet, synodic)
else:
    print "%s is not a superior planet!" % planet
