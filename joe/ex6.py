# x will have the string value "There are 10 types of people."
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said %r." % x
print "I also said '%s'." % y

hilarious = True

# the variable 'joke_evaluation' will have the literal value,
# "Isn't that joke so funny!? %r".
joke_evaluation = "Isn't that joke so funny!? %r"

# the variable 'evaluated_joke' will have the value,
# "Isn't that joke so funny!? True" because the '%r'
# in the joke_evaluation string will have been
# interpolated with the "raw" representation of the
# boolean "True".
evaluated_joke = joke_evaluation % hilarious

# now print that evaluated string
print evaluated_joke

w = "This is the left side of..."
e = "a string with a right side."

# the use of the '+' operator here is called
# "operator overloading". here that character is
# overloaded to mean string concatenation.
print w + e
