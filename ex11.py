print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So you're %r old, %s tall and %r heavy." % (
	age, height, weight)

birth_city = raw_input("In what city or town were you born? ")
birth_country = raw_input("I don't know where %s is. Which country is it located in? ") % birth_city
birth_language = raw_input("What language do they speak in %s? ") % birth_country
language_fake_bool = raw_input("Do you still speak %s? ") % birth_language
def do_you_speak_it():
	if language_fake_bool == 'yes' or 'Yes' or 'YES'
		current_lang = 'and you still speak the native language.';
	elif language_fake_bool == 'no' or 'No' or 'NO'
		current_lang = ', but you no longer speak the native language.';

print "Wow! You were born in %s,which is located in the country of %s. In %s, they speak %s" % (
	birth_city, birth_country, birth_language) + current_lang