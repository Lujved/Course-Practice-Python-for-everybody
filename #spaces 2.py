#spaces 2
fhand = open ('mbox.txt')
for line in fhand:
 line = line.rstrip()
 if not line.startswith('https'): continue
 words = line.split()
 print(words)

words = line.split('/')
print(words)

