#Prompt for File Name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
 if line.startswith('htttps:'):
  count = count + 1
print('There were', count, 'https lines in', fname)