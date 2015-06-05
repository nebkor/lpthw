#Import the argv object into script's global namespace
from sys import argv
# Assigning the variable script and filename to index 0 and 1 respectively
script, filename = argv
# Opening the file given in the argument "filename"
txt = open(filename)
# Printing "Here is your file %r:" using the filename variable
print "Here is your file %r:" % filename
# Reading the file assigned to the txt variable and printing all of that files contents
print txt.read()
# Printing "Type the file name again:"
print "Type the file name again:"
# assigning the output of the raw_input function to the file_again variable
file_again = raw_input ("> ")
# assigning the txt_again variable to the output of the open function on the
# file_again variable
txt_again = open(file_again)
#printing the output of the read function on the txt_again variable
# which is a string that should be a file that is already created
print txt_again.read()