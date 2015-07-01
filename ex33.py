i = 0
numbers = []

# the "inc=1" in the function signature means that if no second argument is
# given, use 1 as the default value.
def i_count(x, inc=1):
        # the "global" keyword lets us refer to a variable outside our local
        # scope, so we use it here to refer to the 'i' variable at the top
        # of the file.
        global i
        # the use of '_' is a convention for, "I'm not going to actually
        # use the value of whatever this is. It's just a syntactic place-
        # holder."
        for _ in range(x):
                if not i < x:
                        break 
                print "At the top i is %d" % i
		numbers.append(i)

                i += inc
                print "Numbers now: ", numbers
                print "At the bottom i is %d" % i

i_count(7, 2)

print "The numbers: "
numbers.sort()
for num in numbers:
	print num
