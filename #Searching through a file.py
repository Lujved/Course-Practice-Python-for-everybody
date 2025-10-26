#Searching through a file
fhand = open('mbox.txt')
for line in fhand:
 if line.startswith ('https:'):
  print(line)
