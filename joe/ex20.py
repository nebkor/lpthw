from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(f):
    # In Python, almost everything is an object, meaning, it is-an
    # instance of a class that inherits, directly or indirectly,
    # from the class "Object". Functions are one of the things
    # in Python that are an object Object members can be created
    # simply by assigning to them, as is done on line 81, below.
    # If this print_a_line() function were called before
    # print_a_line.linecount were created and given a value,
    # it would cause an error.
    print print_a_line.linecount,
    # The argmuent 'f' here is a File object, and the readline()
    # method on File objects causes the File object to be modified.
    # It sets the current position to the character after the next
    # newline. You could see what current position is by having
    # something like "print f.tell()" here.
    print f.readline(),
    # Now that a line has been printed, the print_a_line.linecount
    # instance variable (or member) is incremented by 1.
    print_a_line.linecount += 1

def print_all_lines(f):
    # Set the current position of f to byte 0.
    f.seek(0)
    # current_line is just a local variable, created and
    # referenced only within the print_all_lines() function.
    # It's not like the print_a_line.linecount variable from
    # the print_a_line function.
    current_line = 1
    # The entire 'while' loop is wrapped in a try-block
    # because when the end of the file is reached,f.next()
    # raises the StopIteration exception, and the program
    # shouldn't crash just because it's read the whole file.
    try:
        # f is never actually tested for truth or falseness
        # here. It would be better to say "while True".
        while f:
            # The next() method on the File object
            # is what's called a "generator". It returns the content
            # from the current position up to the next newline, resulting
            # in similar behavior to the readline() method. Except,
            # as stated above, it raises a StopIteration exception
            # once it has returned the last line in the file, which
            # lets you use a try/except block to read the whole thing
            # line-by-line without having to know how many lines are
            # in it beforehand.
            print "%d %s" % (current_line, f.next()),
            current_line += 1
    # Catch the exception thrown by f.next() once the last line is printed.
    except StopIteration
        # A no-op meaning, "Just move along. Nothing to do here."
        pass


current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

# This creates and sets the print_a_line.linecount member variable
# of the function object print_a_line, which was created above with
# "def print_a_line(...)". If the following line were commented
# out, the program would crash with an error once print_a_line()
# were called.
print_a_line.linecount = 1
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)

print
print "Now let's print all the lines:"
# After this line, current_file's current position would be at
# the end of the file, and if you called "print_a_line(current_file)
# again, it would raise an exception and the program would crash.
print_all_lines(current_file)
