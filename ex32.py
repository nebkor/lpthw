the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'appricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
	print "This is the count %d" % number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# creating a list of integers 0 - 5, held by elements
elements = range(0, 6)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i

# reverse a list and print
def reverse_list_print(l):
	print "Now, backwards!"
	l.reverse()
	for i in l:
		print i

print reverse_list_print(elements)