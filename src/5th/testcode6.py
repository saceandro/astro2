#!/usr/bin/env python

planet = raw_input("Planet?: ")
if planet == "Mercury" or planet == "Venus":
    print planet, "is an inferior planet."
elif planet == "Mars" or planet == "Jupiter" or planet == "Saturn"\
         or planet == "Uranus" or planet == "Neptune":
    print planet, "is an superior planet."
elif planet == "Earth":
    print "It is Earth."
else:
    print planet, "is not a solar planet."

    
