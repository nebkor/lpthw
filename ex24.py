print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that to do \n newlines and \t tabs.'

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	booty = "booty"
	return jelly_beans, jars, crates, booty

start_point = 10000
# becomes:
# beans, jars, crates, string_test = 5000000, 10, 1, "booty"
beans, jars, crates, string_test = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10
# start_point is now 1000 (1,000)

print "We can also do it this way:"

# without assigning booty above, adding a %s to the end of the format string creates a vlaueerror.
# values are also run through the function in order. Because the string held by booty
# isn't returned until last, the current implementation of the string print statement
# does not work and results in a typeerror
print "We have %d %s beans, %d jars, and %d crates." % secret_formula(start_point)
