x = []

print type(x)

#list concatenation
y = [1,2,3] + [4,5,6]
y += [7,8]


#Multiplying
x = [1,2,3,4] * 2

x.append(5)

print 'X value: ', x
print 'Y value: ', y
print 'size: ', len(x)
print 2 in x
print x.count(2)
print x.count(5)


a = {'name':'Eudys'}
b = {'name':'Eliel'}
c = {'name':'Aynel'}

z = [a,b,c]

print z

print 'a: in z: ', a in z

print 'hin' in 'many things in the world'

print 
print 
print 

for item in z:

	print item
	print item['name']


print
print
print
print
print 'Minimun: ', min(x)
print 'Maximun: ', max(x)
print 'Sorting: ', sorted(x)
print 'Sum: ', sum(x)
print 'Counting 2: ', x.count(2)
print

#unpacking

names = ['Eudys','Anderson','Bautista','Soto']

a, b, c, d = names
obj1, obj2, obj3 = z



print 'unpacking names print:'
print a
print b
print c
print d
print 

print 'unpacking z print:'
print obj1
print obj2
print obj3

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
hangar1 = [1,2,3,4]
hangar2 = [7,8,9]

print
print 'hangar1: ', hangar1
print 'hangar2: ', hangar2
print 
print 'Extending hangar2'
hangar1.extend(hangar2);
print 'hangar1 extend from hangar2: ', hangar1
