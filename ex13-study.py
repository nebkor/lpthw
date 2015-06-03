from sys import argv

script, my_nose, my_hair, my_legs, my_arms = argv

print """
My nose is very %s but my hair is %s.
When I walk my legs feel like %s and my arms %s around.
""" % (my_nose, my_hair, my_legs, my_arms)

my_feels = raw_input("Do you feel bad about it? ")
print "%s? Well, I didn't care anyway" % my_feels
