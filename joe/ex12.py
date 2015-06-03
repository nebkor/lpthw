age = float(raw_input("How old are you? "))
height = raw_input("How tall are you? ")
weight = float(raw_input("How much do you weigh? "))

print "So you're %r old, %r tall, and %r heavy." % (
    age, height, weight)

print

print "If you gained weight at a constant rate, you",
print "would have had to have gained"
print "%d mass-units per year " % (weight/age),
print "to have achieved your current stature."
