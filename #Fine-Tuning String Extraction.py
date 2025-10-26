#Fine-Tuning String Extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan 5 9:14:15 2008'

import re
y = re.findall('\S+@\S+', x)
print(y)

y = re.findall('^From \S+@\S+', x)
print(y)