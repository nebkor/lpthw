#importing sys.argv into the global namespace as argv
#from sys import argv
# assigning args 1-8 to argv
#args = argv[1:9]

print "Hello World!"
print "Hello Again"
# print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
# print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "Oh my god this will totally help in the long run."
# Creating a dictionary of phrases, indexed by keys 1-8
phrases = {'1': 'Hello World!','2': 'Hello Again','3': 'I like typing this.','4': 'This is fun.',
		'5': 'Yay! Printing.','6': 'I\'d much rather you \'not\'.', '7': 'I "said" do not touch this.',
		'8': 'Oh my god this will totally help me in the long run',}
# using the iteritems method on the dictionary held by the variable phrases
# and assigning k to the key and v to the value of each pair as the for loop
# iterates through each entry in the dictionary. Then the key is printed appended
# by a colon and a space followed by the value corresponding to the key
for k, v in phrases.iteritems():
	print "%s: %s" % (k, v) 
# creates a list of keys from the dictionary assigned to the variable phrases
# then sorts it. The for statement iterates through the list of keys assignging
# i to the output, starting at the first entry, then prints the key appended by :
# followed by the coresponding value in the phrases dictionary
for i in sorted(phrases.keys()):
	print "%s: %s" % (i, phrases[i])
