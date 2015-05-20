# setting the variable 'cars' to 100
cars = 100
# setting the variable 'space_in_a_car' to 4.0
space_in_a_car = 4.0
# setting the variable 'drivers' to 30
drivers = 30
# settings the variable 'passengers' to 90
passengers = 90
# setting the variable 'cars_not_driven' to the value of 'cars - drivers'
cars_not_driven = cars - drivers
# setting the variable of 'cars_driven' to the value of 'drivers'
cars_driven = drivers
# setting the variable 'carpool_capacity' to the value of
# 'cars_driven * space_in_a_car'
carpool_capacity = cars_driven * space_in_a_car
# setting the variable 'average_passengers_per_car' to the value of
# 'passengers / cars_driven'
average_passengers_per_car = passengers / cars_driven

# prints the string 'There are 100 cars available.'
print "There are", cars, "cars available."
# prints the string 'There are only 30 drivers available.'
print "There are only", drivers, "drivers available."
# 
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."