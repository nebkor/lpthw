# count up to 100 from 1, printing each number, if divisible by 3 - print richard, if divisible by 7
# print is, if divisible by 21 print awesome

for i in xrange(1, 101):
    if i % 21 == 0:
        print "Awesome"
    elif i % 7 == 0:
        print "Is"
    elif i % 3 == 0:
        print "Richard"
    else:
        print i
