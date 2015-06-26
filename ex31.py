print "You enter a dark room with two doors. Do you go through door #1 or #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheesecake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Re-evaluate why you were opening strange doors in dark rooms."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "The darkness becomes too much for you, so you leave the area."
	else:
		print "What is a '%s'? The bear eats your face off. Good job." % bear

elif door == "2":
	print "You stare into the endless abyss at Cthulu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	elif insanity == "3":
		print "Cthulu wonders why you haven't heard of Revolver, then tosses you a vinyl record."
		print "What are you supposed to do with that?"
	else:
		print "Insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"
