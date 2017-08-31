import json
a = [{'a':1,'b':2}]
print a
print type(a)

b = {'c':1,'d':2}
a.append(b)
print a
print type(a)
c = json.dumps(a)
print c
print type(c)
