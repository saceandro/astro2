#!/usr/bin/env python

length1=10.
length2=3.

format1="%s/%s is %010.4f"
format2="%s/%s is %-10.2f"
format3="%s/%s is %+10.4f"
format4="%s/%s is %10.4f"

div=length1 / length2

print format1 % (length1,length2,div)
print format2 % (length1,length2,div)
print format3 % (length1,length2,div)
print format4 % (length1,length2,div)
