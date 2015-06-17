from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(f):
    # see http://xahlee.info/perl-python/stateful_func.html
    print print_a_line.linecount,
    print f.readline(),
    print_a_line.linecount += 1

def print_all_lines(f):
    f.seek(0)
    current_line = 1
    try:
        while f:
            print "%d %s" % (current_line, f.next()),
            current_line += 1
    except StopIteration:
        pass


current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

print_a_line.linecount = 1
print_a_line(current_file)
print_a_line(current_file)
print_a_line(current_file)

print
print "Now let's print all the lines:"
print_all_lines(current_file)
