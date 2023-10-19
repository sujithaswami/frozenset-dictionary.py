a={1,2,3}
b={5,2,7}
print(a.union(b))

#intersection

#Syntax:variable.intersection(variable)

a={1,2,3}
b={5,2,7}
print(a.intersection(b))


#intersection update

#Syntax:set1.intersection.update(set2)

a={'a','b','c'}
b={'b','c','e'}
print(a.intersection_update(b))
print(a)
print(b)

#isdisjoint

#syntax:set1.isdisjoint(set2)

a={'a'}
b={'d'}
print(a.isdisjoint(b))

a={'a'}
b={'a'}
print(a.isdisjoint(b))

#difference

#syntax:set1.difference(set2)

a={'anu', 'madhu','suji', 'durga'}
b={'suji', 'durga'}
print(a.difference(b))

#symmetric

#syntax:set1.symmetric difference(set2)

a={'anu', 'madhu','suji', 'durga'}
b={'anu','Madhu'}
print(a.symmetric_difference(b))

#symmetric difference update

#syntax:set1.symmetric difference update(set2)

a={'durga','anu', 'madhu','suji'}
b={'anu','suji'}
print(a.symmetric_difference_update(b))
print(a)
print(b)

#issubset

#syntax:set1.issubset(set2)

a={'durga','anu', 'madhu','suji'}
b={'suji','madhu'}
print(a.issubset(b))

a={'durga', 'anu', 'madhu','suji'}
b={'durga','anu', 'madhu','suji'}
print(a.issubset(b))

#issuperset

#syntax:set1.issuperset(set2)
a={'durga', 'anu', 'madhu','suji'}
b={'anu'}
print(a.issuperset(b))