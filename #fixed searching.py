#fixed searching
fhand = open('mbox.txt')
for line in fhand:
 line = line.rstrip()
 if line.startswith('https:'):
  print(line)
