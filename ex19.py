# defining a function named "cheese_and_crackers()" which takes the arguments
# cheese_count and boxes_of_crackers. The function prints the string
# "You have" appended by the numeric representation of cheese_count
# followed by "cheeses!". Then prints "You have" appended by the
# numeric representation of boxes_of_crackers followed by "boxes of crackers!".
# Then the string "Man, that's enough for a party!" is printed followed
# by "Get a blanket." with an additional new line.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket.\n"
# prints the string "We can just give the function numbers directly:"
print "We can just give the function numbers directly:"
# calls the function "cheese_and_crackers()" using integers
# 20 and 30 as it's arguments
cheese_and_crackers(20, 30)
# prints the string "Or we can use variables from our script:"
print "Or we can use variables from our script:"
# assigning the variable amount_of_cheese to the integer value 10
amount_of_cheese = 10
# assigning the variable amount_of_crackers to the integer value 50
amount_of_crackers = 50
# calls the function "cheese_and_crackers()" using the variables
# amount_of_cheese and amount_of_crackers which is represented
# as "cheese_and_crackers(10, 50)"
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# prints the string "We can even do math inside too:"
print "We can even do math inside too:"
# calls the function "cheese_and_crackers()" using the return of
# 10 + 20 and 5 + 6 as it's arguments
cheese_and_crackers(10 + 20, 5 + 6)
# prints the string "And we can combine the two, variables and math:"
print "And we can combine the two, variables and math:"
# calls the function "cheese_and_crackers()" using the variable 
# "amount_of_cheese + 100" and "amount_of_crackers + 1000" 
# represented as "cheese_and_crackers(110, 1050)"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
