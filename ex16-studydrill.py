from sys import argv

files_to_be_read = argv[1:]

print "Here are the file(s) you'd like to read:\n"
for i in files_to_be_read:
	print "%s" % i
print "\n"
print "This is the end of this script" 