# Import the argv object into script's global namespace
from sys import argv
# Assigning the variable script and filename to index of argv 0 and 1 respectively
script, filename = argv
# Assigns the variable txt to the file object which is the return value
# of the open() function using the variable filename as it's argument
txt = open(filename)
# Printing "Here is your file " followed by the raw representation of the
# string variable filenaame followed by a :
print "Here is your file %r:" % filename
# Prints the output of the read method on the file object assigned to the variable txt
print txt.read()
txt.close()
# Printing "Type the file name again:"
print "Type the file name again:"
# assigning the output of the raw_input function to the file_again variable
file_again = raw_input ("> ")
# Assigns the variable txt_again to the output of the open() function
# using the variable file_again as it's argument
txt_again = open(file_again)
# printing the output of the read() method on the txt_again variable
# which is a string that should be a file that is already created
print txt_again.read()
txt_again.close()

# remember: Opening a file using the write mode will truncate
# (a.k.a erase) any existing data