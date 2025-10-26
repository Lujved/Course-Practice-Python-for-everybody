#Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

#Count word frequency
count = dict()
for line in handle: 
 words = line.split()
 for word in words:
  count[word] = count.get(word, 0) + 1

#find the most common word
bigcount = None
bigword = None
for word, count in count.items():
 if bigcount is None or count > bigcount:
  bigword = word
  bigcount = count

#All done
print(bigword, bigcount)
