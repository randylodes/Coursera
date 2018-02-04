

# Using .split with strings
abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

for w in stuff:
    print(w)

# default split is space; multiple spaces re treated as one 

# using another delimiter character
line = 'first;second;third'
w = line.split(';')
print(w[:1])

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    print(words[2])

# The double split
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    print(email)
    host = email.split('@')[1]
    print(host)
