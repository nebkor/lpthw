def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# the function "subtract()" takes the numeric arguments a and b.
# "subtract()" then prints, "SUBTRACTING" followed by the integer value
# of a, then a "-", followed by the integer value of b. Finally,
# the function returns the [possibly floating point] difference of a and b
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

# like subtract(), but with the arithmetic product of a and b.
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

# like multiply, but with the arithmetic division of a and b
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

# playing with floating points.
age = add(30.5, 5)
height = subtract(78, 4.3)
weight = multiply(90.99, 2)
iq = divide(100, 1.1)

# %d prints only the integer portion of a numeric value.
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
	age, height, weight, iq)

# wanted to see the raw value of age and weight after being
# returned by the function
print age, weight

# A puzzle for extra credit, type it in anyway.
print "Here is a puzzle."

# Written out by hand, the equation looks like:
# what = 35 + (74 - (180 * (50 / 2)))
# Confirmed in python interpreter: what = -4391
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", "%.2f\n" % what, "Can you do it by hand?"

# Exercise 4
what = 150 - (35 + (400 * (2 / 3)))
print what
# ^^^ returns different value if ((())) are not present as I am not following
# the order of operations in this equation

# assigning the variable "what" to the return of....
# fuck I wrote all this backwards ><
# calling the "divide()" function using 2 and 3 as its arguments, a and b. Then
# calling the "multiply()" function on the value returned by "divide()" as b and 400 as a,
# then calling the "add()" function on the returned value of "multiply()" as b and 35 as a,
# finally calling the "subtract()" function using the returned value of the "add()" function
# as b and 150 as a
what = subtract(150, add(35, multiply(400, divide(2, 3))))
print what

# ^^^ what are better ways to write things like this?
# Joe says: writing out the "regular, by-hand" (like you did on line 43)
# way of the nested function calls is a good way to demonstrate exactly
# what the code is *supposed* to be doing. It's a good method for
# explaining any block of code that is doing something familiar in an
# unfamiliar way.
