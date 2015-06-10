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
print "If your pizza is %s inches diagonally, then the pizza is %s inches around!" % (
	pizza_diameter, pizza_cir)