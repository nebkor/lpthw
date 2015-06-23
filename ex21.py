def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

# creating the function "subtract()" which takes the arguments a and b.
# "subtract()" then prints, "SUBTRACTING" followed by the integer value
# of a, then a "-", followed by the integer value of b. Finally,
# the function returns the difference of a and b
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

print "Let's do some math with just functions!"

# playing with floating points. %d only returns integers without rounding
age = add(30.5, 5)
height = subtract(78, 4.3)
weight = multiply(90.99, 2)
iq = divide(100, 1.1)

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