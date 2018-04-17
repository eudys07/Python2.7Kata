x = []

print type(x)

#list concatenation
y = [1,2,3] + [5,6]
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


