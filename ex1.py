#importing sys.argv into the global namespace as argv
#from sys import argv
# assigning args 1-8 to argv
#args = argv[1:9]

print "Hello World!"
print "Hello Again"
#print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
#print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
print "Oh my god this will totally help in the long run."
#Creating a dictionary of phrases, indexed by keys 1-8
phrases = {'1': 'Hello World!','2': 'Hello Again','3': 'I like typing this.','4': 'This is fun.',
		'5': 'Yay! Printing.','6': 'I\'d much rather you \'not\'.', '7': 'I "said" do not touch this.',
		'8': 'Oh my god this will totally help me in the long run',}

for k, v in phrases.iteritems():
	print "%s: %s" % (k, v) 

for i in sorted(phrases.keys()):
	print "%s: %s" % (i, phrases[i])
