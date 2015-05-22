name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
intocm = 2.54
lbtokg = 1.0 / 2.2

print "Let's talk about %s." % name
print "He's %d centimeters tall." % (height * intocm)
print "He's %d kilograms heavy." % (weight * lbtokg)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d" % (
	age, height, weight, age + height + weight)

