from sys import argv

# set 'args' to the 1th slice of sys.argv; it's just the arguments without
# the script name.
args = argv[1:]

# The first element of sys.argv, like any array, is at index 0. sys.argv[0]
# is always the name of the script as it was invoked. What happens if you
# make a symlink to this file and call it like "python symlinked-ex13-arg.py",
# assuming that was name of the symlink you made to it? What is the script name
# when you just run the "python" command to get an interactive REPL?
#
# The builtin "len()" function can take any sequence-like object (eg, lists,
# strings, etc.). It returns the number of elements in the sequence.
print
print "This script is called %s, and it has %d arguments:" % (argv[0], len(args))
print args

if len(args) > 0:
    print
    print "Or, more prettily:"
    print
# it's not strictly required to have an else-clause, but it makes your meaning
# unambiguous.
else:
    pass

# the range() function takes at least one argument, the number to count up to
# (but not actually get to) from zero. Try typing "range(5)" without the quotes
# in a python REPL. Try giving more than one argument (eg, "range(1, 10)" or
# "range(-5, 6, 2)").
for i in range(len(args)):
    argnum = i + 1
    print " %d: %s" % (argnum, args[i])

print # a naked print statement just prints a blank line

print "And that's that!\n"
