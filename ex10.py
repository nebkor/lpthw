tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# playing with more complex formatting per study drill 3
print "%s\n%s\"%s\"%s" % (tabby_cat, persian_cat, backslash_cat, fat_cat)
# Using %r to see the demonstrate the differences between the string format
# and the raw format
print "%r\n%r\"%r\"%r" % (tabby_cat, persian_cat, backslash_cat, fat_cat)


# A tiny piece of code to try out from the book
#while True:
#	for i in ["/", "-", "|", "\\", "|"]:
#		print "%s\r" % i,

# note s for later CAPITOLIZE T IN TRUE
# make sure to commit when the original 
# exercise is complete, before adding anything

# NEVER FORGET YOUR PROPER PUNCTUATION. 
# We wasted a good 5 minutes trying to fix a non existant issue