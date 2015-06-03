from sys import argv

args = argv[1:]

print "This script is called %s, and it has %d arguments:" % (argv[0], len(args))
print args

if len(args) > 0:
    print
    print "Or, more prettily:"
    print
else:
    pass

for i in range(len(args)):
    j = i + 1
    print " %d: %s" % (j, args[i])

print

print "And that's that!\n"
