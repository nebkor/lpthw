#!/usr/bin/env python

LB2KG = 1.0 / 2.2
INCH2CM = 2.54

name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %#x cm tall." % (height * INCH2CM) # "0x" hexidecimal format char
print "He's %d kg heavy." % (weight * LB2KG)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)
