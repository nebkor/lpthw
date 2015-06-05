from sys import argv

script, user_name, mood = argv
prompt = '* '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I see youre in a %s mood, but I'd like to ask you a few questions." % mood
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "What room of the house is your computer in?"
comp_room = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have %r computer. Nice.
I bet your computer likes being in the %r.
""" % (likes, lives, computer, comp_room)