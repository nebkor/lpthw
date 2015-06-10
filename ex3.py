# The line below prints the string "I will now count my chickens:" followed by a new line
print "I will now count my chickens:"
# evalutates 25 + (30 / 6) then prints the string "Hens" followed by a space 
# followed by the result of the arithmatic expression
print "Hens", 25 + 30 / 6
# 100 - ((25 * 3) % 4) -> 100 - (75 % 4) -> 100 - 3 -> 97
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"
# (3 + 2 + 1 - 5) + (4 % 2) - (1 / 4) + 6
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# Prints the string
print "Is it true that 3 + 2 < 5 - 7?"
# (3 + 2) < (5 - 7) -> 5 < -2 -> False
print 3 + 2 < 5 - 7
# The line below prints "what is 3 + 2?" followed by a space followed by a 5
print "What is 3 + 2?", 3 + 2
# prints "what is 5 -7?" followed by a space followed by -2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False"
# 
print "How about some more."
# Prints "Is it greater?" followed by a space followed by True
print "Is it greater?", 5 > -2
# prints "Is it greater or equal?" followed by a space followed by True
print "Is it greater or equal?", 5 >= -2
# prints "Is it less or equal?" followed by a space followed by False
print "Is it less or equal?", 5 <= -2

#Pizza circumference from diameter
#import sys.arvg into the namespace as argv
from sys import argv

# Set variable pizza to the second item (first user given argument) in the argv list
pizza_diameter = argv[1]
#turn the value of pizza_diameter into an integer
pizza_diameter_int = int(pizza_diameter)
# multiply pizza_diameter_int by 3.14 and assign the output to pizza_cir
pizza_cir = 3.14 * pizza_diameter_int

# prints "If your pizza is" then the value of pizza_diameter followed by
# "inches diagonaly, then the pizza is" then the value of pizza_cir followed by
# "inches around!"
print "If your pizza is %s inches diagonaly, then the pizza is %s around!" % (
	pizza_diameter, pizza_cir)