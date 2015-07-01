i = 0
numbers = []

def i_count(x, inc=1):
        global i
	while i < x:
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
