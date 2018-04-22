#Tulples

print 'Creating new tuple'
print 'x = ()'
x = ()
print 'y = 1,2,3'
y = 1,2,3
print 'z = 1,'
z = 1,
print 'tuple(list1)'
print
print
list1 = [1,2,3]
tuple1 = tuple(list1)
tuple2 = tuple(list1)


print 'tuple1'
print tuple1
print 'tuple2'
print tuple2


print
print 'deleting item from tuple: error due to inmutable structure'
print
print
print 'del(tuple1[1]):  TypeError: tuple object does not support item deletion' 
#del(tuple1[1])
print 'tuple1[1] = 5 :  TypeError: tuple object does not support item assignment' 
#tuple1[1] = 5


print 'deleting tuple2'
print
print 'asking for tuple2 before deleting'
tuple2
print 'del(tuple2)' 
del(tuple2)
print 'asking for tuple2 after deleting:    NameError: name tuple2 is not defined'
#tuple2

print
print
tuple3 = 1,['a','b','c'], 3, 4,
print 'modifiying a list inside a tuple'
print
print 'tuple3'
print tuple3
print 

print 'Inserting value in list inside of tuple3' 
tuple3[1].insert(3,'d')
tuple3[1].insert(4,'e')
print 'tuple3'
print tuple3
print

print 'modifiying the position 4 in the list inside of tuple3'
tuple3[1][4] = 'work'
print 'tuple3'
print tuple3
print

print 'deleting popsition 4 from the list inside of tuple3'
del(tuple3[1][4])
print 'tuple3'
print tuple3


