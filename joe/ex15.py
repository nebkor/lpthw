# import sys.argv into the global namespace as argv
from sys import argv

# assign to the 'script' variable the value of argv[0],
# assign to the 'filename' variable the value of argv[1]
script, filename = argv

# assign to the 'txt' variable the value returned by the
# function "open()", which was called with the variable
# 'filename' as its argument. The "open()" function returns
# a File object, so the variable 'txt' has a value of type
# "File".
txt = open(filename)

# print the raw representation of the string value
# of the variable 'filename', prepended with the string,
# "Here's your file " and appended by the string ":".
print "Here's your file %r:" % filename
# print the contents of the file named by the value
# of the variable 'filename', by invoking the "read()"
# method of object referenced by the variable 'txt'.
print txt.read()

# close the file handle referenced by the variable 'txt'
# by calling the "close()" method. calling "read()" on
# txt after it's been closed would be an error.
txt.close()

# prints the string "Type the filename again:"
print "Type the filename again:"
# assign to the variable 'file_again' the output from
# the function "raw_input()", which was called with a string
# argument "> ", used as the prompt for the user
# to enter a string to be passed as input to the "raw_input()"
# function
file_again = raw_input("> ")

# assgin to the 'txt' variable the value returned by the
# function "open()", which was called with the variable
# 'file_again' as its argument.
txt_again = open(file_again)

print txt_again.read()

txt_again.close()
