# Importing sys.argv into the global namespace as argv
from sys import argv

# assigning the variable files_to_be_read to the list returned from
# the 2nd slice of argv onward
files_to_be_read = argv[1:]

print "Here are the file(s) you'd like to read:\n"
for i in files_to_be_read:
	print "%s" % i
	print
	print open(i, 'r').readlines()












print "This is the end of this script" 