# variable creating a string "There are 10 types of people"
x = "There are %d types of people." % 10
# setting the variable binary to the string "binary"
binary = "binary"
# setting the variable do_not to the string "don't"
do_not = "don't"
# variable setting the string "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)

# printing the string "There are 10 types of people"
print x
# printing the string "Those who know binary and those who don't."
print y
# printing the string "I said: 'There are 10 types of people.'."
print "I said: %r." % x
# printing the string "I also said: 'Those who know binary and those who don't.'."
print "I also said: '%s'." % y
# setting the hilarious variable to boolean "False"
hilarious = False
# setting the variable 'joke_evaluation' to "Isn't that joke so funny?! %r"
joke_evaluation = "Isn't that joke so funny?! %r"
# printing a test of the variable 'joke_evaluation' to see the effects of
# %r without anything to format
print joke_evaluation
# printing the string  "Isn't that joke so funny?! False"
print joke_evaluation % hilarious
# setting the variable w to the string "This is the left side of..."
w = "This is the left side of..."
# setting the variable e to "a string with a right side"
e = "a string with a right side."
# printing the string "This is the left side of...a string with a right side." 
# this is called string cancattonation 
print w + e