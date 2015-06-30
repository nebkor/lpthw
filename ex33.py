i = 0
numbers = []

def i_count(a, b):
	while b > a:
		print "a is currently:", a
		numbers.append(a)
		if not a > b:
			a += 1
			print "now a is:", a
		else:
			pass

i_count(0, 56)


#while i < 8:
#	print "At the top i is %d" % i
#	numbers.append(i)
#
#	i = i + 1
#	print "Numbers now: ", numbers
#	print "At the botom i is %d" % i

print "The numbers: "
numbers.sort()
for num in numbers:
	print num,
