set={1,1,2,3,"P","S"}
print(type(set))
print(set) #Print unorder set without repetation
print(len(set)) #SET DON"T ALLOW DUPLICATE VALUES

#Set Methods
set.add(4) #To add
print(set)

set.remove(2)
print(set)

print(set.pop())
print(set.pop())

set.clear()
print(set)

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1.intersection(set2))