x = []

print 'type x'
print type(x)
print
print

print 'list concatenation'
y = [1,2,3] + [4,5,6]
y += [7,8]
print
print

print 'Multiplying'
x = [1,2,3,4] * 2
print
print

print 'append'
x.append(5)

print 'X value: ', x
print 'Y value: ', y
print
print

print 'len'
print 'size: ', len(x)
print
print

print 'Checking membership'
print '2 in x?'
print 2 in x
print '2 not in x?'
print 2 not in x
print
print

print 'count'
print x.count(2)
print x.count(5)


a = {'name':'Eudys'}
b = {'name':'Eliel'}
c = {'name':'Aynel'}

z = [a,b,c]
print z
print
print

print 'checking membership with object: '
print 'a: in z: ', a in z

print

print 'checking membership with string: '
print 'hin' in 'many things in the world'

print
print 'printing item from list'
print
for item in z:
	print 'whole item:', item
	print 'item attibute name: ', item['name']


print
print 'Minimun: ', min(x)
print 'Maximun: ', max(x)
print 'Sorting: ', sorted(x)
print 'Sum: ', sum(x)
print 'Counting 2: ', x.count(2)
print


print
print 'unpacking'
names = ['Eudys','Anderson','Bautista','Soto']
print 'names: ', names
print

a, b, c, d = names
print 'unpacking names in a,b,c,d: '
print 'a: ', a
print 'b: ', b
print 'c: ', c
print 'd: ', d


print
print
obj1, obj2, obj3 = z
print 'unpacking objects in z in obj1, obj2, obj3'
print 'obj1: ', obj1
print 'obj2: ', obj2
print 'obj3: ', obj3


print
print
print 'List Comprehension'
#list Comprehension
x = [m for m in range(10)]
print x

y = [m for m in range(20) if m%2]
print y

print 'this is z: ', z
del(z[0])
print 'this is now z: ', z
print
print 'printign 0 index in z: ', z[0]
print 'deleting z'
#del(z)
print
print
print 'this is now z: '
print z

print
print
hangar1 = [1,'@',2,'@',3,4]
hangar2 = [7,8,9]

print
print 'hangar1: ', hangar1
print 'hangar2: ', hangar2
print 
print 'Inserting a 5 in the index 0 in hangar2'
hangar2.insert(0,5)
print 'hangar2: ', hangar2
print 
print 'Inserting a 6 in the index 1 in hangar2'
hangar2.insert(1,6)
print 'hangar2: ', hangar2
print 
print 
print 'Extending hangar2'
hangar1.extend(hangar2);
print 'hangar1 extend from hangar2: ', hangar1
print 
print 

print 'using pop:' 
hangar1.pop()
print hangar1
print 
print 

print 'using remove:' 
hangar1.remove('@')
print hangar1
print
print 'using remove again:' 
hangar1.remove('@')
print hangar1
print 
print 

print 'using reverse:' 
hangar1.reverse()
print hangar1
print 
print 

print 'using sort:' 
hangar1.sort()
print hangar1
print 
print 
