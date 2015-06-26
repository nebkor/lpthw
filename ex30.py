# Assigns the variable people to the value of 30
people = 30
cars = 40 # assigns cars to the value of 40
trucks = 15 # assigns trucks to the value of 40

# A function named "return40()" which prints, "This is 'return40()'"
# and returns 40
def return40():
	print "This is 'return40()'"
	return 40

# Checks if cars is greater than people, if true, prints
# "We should take the cars."
if cars > people:
	print "We should take the cars."
# Checks to see if 40 is less than people, if true, prints
# "We should not take the cars"
elif return40() < people: 
	print "We should not take the cars."
else: # prints "We can't decide." if previous statements are false
	print "We can't decide."

# takes the value of trucks and adds 50 to it.
trucks += 50

if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we should take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."
else:
	print "Fine, let's stay home then."
