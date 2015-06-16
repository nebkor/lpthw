from sys import argv, exit
from os.path import exists

from_file, to_file = argv[1:3]

indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata)
try:
	if exists(to_file) == True:
		raise IOError("The destination file already esists")
	else: 
		open(to_file, 'w').write(indata)
except IOError as error:
	print error
	exit(15)


print "Copied content from %s to %s" % (
	from_file, to_file)