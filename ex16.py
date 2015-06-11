from sys import argv
# assigning the variable script to argv[0] and the variable
# filename to argv[1]
script, filename = argv

# print "We're going to erase" appended by the output of
# the variable filename
print "We're going to erase %r" % filename
print "If you don't want that, hit CTRL-C (^C)." # printing a string
print "If you do want that, hit RETURN" # printing a string
# using the function "raw_input()" to create a stopping point
# in the script so the user can stop the script before any files
# are overwritten
raw_input("?")

print "Opening the file..." # printing a string

# assigning the variable target to the writable file object
# returned by the "open()" function 
target = open(filename, 'w')

print "Truncating the file. Goodbye!" # printing a string
# using the "truncate()" method on the output of the target variable
target.truncate()

print "Now I'm going to ask you for three lines." # printing a string

# assigning the variable line1 to the string input provided by the user
# and captured by the "raw_input()" function
line1 = raw_input("line 1: ") 
# assigning the variable line2 to the string input provided by the user
# and captured by the "raw_input()" function
line2 = raw_input("line 2: ")
# assigning the variable line3 to the string input provided by the user
# and captured by the "raw_input()" function
line3 = raw_input("line 3: ")

print "I'm going to write these to the file." # printing a string

# using the "write()" method on the file object held by the variable target
# to write the string output of line1, line2, and line3, each followed by
# a new line
target.write('%s\n%s\n%s' % (line1, line2, line3))


print "And finally, we close it." # printing a string
# using the "close()" method on the file object held by the variable
# target
target.close()