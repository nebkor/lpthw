# Importing sys.argv into the global namespace as argv
from sys import argv

# assigning the variable files_to_be_read to the list returned from
# the 2nd slice of argv onward
files_to_be_read = argv[1:]

# Prints "Here are the file(s) you'd like to read:" with a trailing new line
print "Here are the file(s) you'd like to read:\n"
# Iterates through the variable files_to_be_read which holds a list 
# of arguments given to the script then prints the name of the file
# appended by a ":" followed by a new line and then it's contents before
# moving to the next entry in the list
for i in files_to_be_read:
	print "%s:\n" % i
	f = open(i, 'r')
	print f.read()
	print
	f.close()

print "This is the end of this script" 