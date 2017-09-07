# for i in range(4):
#     name='v'+str(i)
#     locals()['v'+str(i)]=[]
#
# print v1,v2,v3
# # print locals()[ 'V'+str(i)]
#
# names = locals()
# for i in xrange(1, 101):
#     names['x%s' % i] = i
#
# print names['x%s' % i]

process_num = 5
results = []
names = locals()
for i in range(1,process_num):
    names['result%s' % i] = []
for j in range(1,process_num):
    names['input%s' % j] = []
print '*****'
print input1
print type(input1)
