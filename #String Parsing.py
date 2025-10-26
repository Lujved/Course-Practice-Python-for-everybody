#String Parsing
data = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find('', atpos)
print(sppos)

host = data[atpos+1: sppos]
print(host)

line = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008'
words = line.split()
email =words[1]
pieces = email.split('@')
print(pieces[1])

import re
lin = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:16 2008'
y = re.findall('^From .*@([^ ]*)', lin)
print(y)
