#Set

print 'Creating new set'
print 'x = {}'
x = {}
print 'y = {1,2,3}'
y = {1,2,3}
print 'z = 1,'
z = 1,
print 'set(list1)'
print
print
list1 = [1,2,3,4,3,2]
set1 = set(list1)
set2 = set(list1)


print 'set1'
print set1
print 'set2'
print set2

set3 = {m for m in range(50) if m%2}
print
print 'set3'
print set3

print 
print 'len(set3)'
print len(set3)

print 
print 'set3.pop()'
print set3.pop()
print
print 'set3'
print set3
print 
print 'set3.pop() again'
print set3.pop()
print
print 'set3'
print set3

print
print 'Checking membership'
print '5 in set3'
print 5 in set3
print
print '4 in set3'
print 4 in set3