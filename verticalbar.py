import re

s = input()

r = re.compile('red flag|blue flag')

m = r.findall(s)
print(list(m))
