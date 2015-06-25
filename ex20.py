# import sys.argv into the global namespace as argv
from sys import argv

# assign script to the 0th entry in the argv array and input_file 
# to the 1th entry in the argv array
script, input_file = argv

# Define the function "print_all()" which takes an argument as f
def print_all(f):
	print f.read() # prints the contents of f using the .read() method
				   # f can only be a file object, else the .read() method will fail

# Define the function "rewind()" which takes an argument as f
def rewind(f):
	f.seek(0) # using the .seek() method on a file object to
			  # return the offset of the file back to the 0th byte

# define the function "print_a_line()" which takes two arguments as
# line_count and f. 
def print_a_line(line_count, f):
	print line_count, f.readline(), # prints the raw value of line_count followed by a space
									# then uses the .readline() method on the file object f 
									# to print a string from the the file object starting at the current
									# offset until the next new line

# assigning the variable current_file to the output of the "open()" function
# using the input_file variable as it's argument
current_file = open(input_file)

print "First let's print the whole file:\n"

# calls the "print_all()" function on the file object held by the 
# current_file variable, which performs the .read() method from the 
# file object's current offset to the end of the file.
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# calls the "rewind()" function on the file object held by the
# current_file variable which performs the .seek() method on the file object
# setting offset of the file object back to the 0th byte
rewind(current_file)

print "Now let's print three lines:"

current_line = 1 # current_line value is 1
print_a_line(current_line, current_file)
current_line = current_line + 1 # current_line value is now 2
print_a_line(current_line, current_file)
current_line = current_line + 1 # current_line value is now 3
print_a_line(current_line, current_file)

print_a_line(current_line, f = open(input_file))
print_a_line(current_line + 1, current_file)
print_a_line(current_line + 2, current_file)