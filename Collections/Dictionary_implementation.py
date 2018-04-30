#Dictionary

print
print 'Creating new Dictionary'
print
dict1 = {'name':'Eudys','lastname':'Bautista','age':31}
dict2 = dict([('name','Aynel'),('lastname','Bautista'),('age',28)])
dict3 = dict(name='Eliel',lastname='Garcia',age=32)


print 'dict1: '
print dict1
print 'dict2: '
print dict2
print 'dict3: '
print dict3

print
print 'Dictionary operations: '
print
print

print 'Adding or change item in dic2: '
print 'dict2[age] = 29: '
print dict2['age']
dict2['age'] = 29
print ''
print 'dict2: ', dict2
print

print
print 'deleting item in the list'
del dict2['age']
print ''
print 'dict2: ', dict2
print

print
print 'dict len'
print ''
print 'len(dict2): ', len(dict2)
print

print
print 'checking membership in dict2'
print ''
print '(name, Aynel) in  dict2: ', ('name', 'Aynel') in  dict2
print ''
print '(name, Aynel) not in  dict2: ', ('name', 'Aynel') not in  dict2
print

print
print 'clearing dict2'
print ''
print 'dict2.clear(): ', dict2.clear()
print
print 'dict2: ', dict2
print



print
print
print 'ACCESSING KEYS AND VALUES IN A DICT'

print
print 'Return list of keys in dict1'
print 'dict1.keys(): ', dict1.keys()
print

print
print 'Return list of values in dict1'
print 'dict1.values(): ', dict1.values()
print

print
print 'Return list of key-value tuple pairs in dict1'
print 'dict1.items(): ', dict1.items()
print

print
print 'Checking membership in dict1: '
print 'Eudys in dict1.values(): ', 'Eudys' in dict1.values()
print
