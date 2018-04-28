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

print
print 'removing item'
print 'existing item: set.remove(5)'
print set3.remove(5)
print
print 'not existing item: set.remove(4): KeyError: 4'
#print set3.remove(4)


print
print 'Adding item to set'
print 'same type: set3.add(4)'
print set3.add(4)
print
a = 'Work'
print "a = 'Work'"
print 'different type: set3.add(a)'
print set3.add(a)
print
print 'Clearing the set'
print 'set3.clear()'
print set3.clear()
print
print 'set3'
print set3

print
print
print 'STANDARD MATHEMATICAL SET OPERATION'
print 
print 'For this let going to create 3 new sets: math_set1, math_set2 and math_set3, math_set4 '
math_set1 = {1,2,3,4,5}
math_set2 = math_set1
math_set3 = {'one', 'two', 'Theree'}
math_set4 = {'one',1, 2,'two',3, 'Theree'}
print 
print 'math_set1'
print math_set1
print 'math_set2'
print math_set2
print 'math_set3'
print math_set3
print 'math_set4'
print math_set4

print 
print 
print '------------------------------------------'
print "Insertion(AND) '&'"
print 'math_set1 & math_set2'
print math_set1 & math_set2
print
print 'math_set1 & math_set3'
print math_set1 & math_set3
print
print 'math_set1 & math_set4'
print math_set1 & math_set4
print
print 'math_set3 & math_set4'
print math_set3 & math_set4

print 
print 
print '------------------------------------------'
print "Union(OR) '|'"
print 'math_set1 | math_set2'
print math_set1 | math_set2
print
print 'math_set1 | math_set3'
print math_set1 | math_set3
print
print 'math_set1 | math_set4'
print math_set1 | math_set4
print
print 'math_set3 | math_set4'
print math_set3 | math_set4

print 
print 
print '------------------------------------------'
print "Symmetric difference(XOR) '^'"
print 'math_set1 ^ math_set2'
print math_set1 ^ math_set2
print
print 'math_set1 ^ math_set3'
print math_set1 ^ math_set3
print
print 'math_set1 ^ math_set4'
print math_set1 ^ math_set4
print
print 'math_set3 ^ math_set4'
print math_set3 ^ math_set4

print 
print 
print '------------------------------------------'
print "Difference '-'"
print 'math_set1 - math_set2: in math_set1 but not in math_set2'
print math_set1 - math_set2
print
print 'math_set1 - math_set3: in math_set1 but not in math_set3'
print math_set1 - math_set3
print
print 'math_set3 - math_set1: in math_set3 but not in math_set1'
print math_set3 - math_set1
print
print 'math_set1 - math_set4: in math_set1 but not in math_set4'
print math_set1 - math_set4
print
print 'math_set4 - math_set1: in math_set4 but not in math_set1'
print math_set4 - math_set1
print
print 'math_set3 - math_set4: in math_set3 but not in math_set4'
print math_set3 - math_set4
print
print 'math_set4 - math_set3: in math_set4 but not in math_set3'
print math_set4 - math_set3
print
print

print '------------------------------------------'
print "Subset '<='"
print 'math_set1 <= math_set2: math_set1 contains math_set2'
print math_set1 <= math_set2
print
print 'math_set1 <= math_set3: math_set1 contains math_set3'
print math_set1 <= math_set3
print
print 'math_set1 <= math_set4: math_set1 contains math_set4'
print math_set1 <= math_set4
print
print 'math_set3 <= math_set4: math_set3 contains math_set4'
print math_set3 <= math_set4
print
print


print '------------------------------------------'
print "Superset '>=' "
print 'math_set1 >= math_set2:'
print math_set1 >= math_set2
print
print 'math_set1 >= math_set3'
print math_set1 >= math_set3
print
print 'math_set1 >= math_set4'
print math_set1 >= math_set4
print
print 'math_set3 >= math_set4'
print math_set3 >= math_set4






