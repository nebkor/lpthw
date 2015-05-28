formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.", # The output is double quoted still because 
	"So I said goodnight." # the string contains an apostrophe.
)

# mistake note: Don't forget the damn comma....