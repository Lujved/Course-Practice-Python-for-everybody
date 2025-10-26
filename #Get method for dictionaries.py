#Get method for dictionaries
counts = dict()
names = ['csev', 'cwen', 'csev', 'rqian', 'cwen']
for name in names:
 counts[name] = counts.get(name, 0) + 1
print(counts)
