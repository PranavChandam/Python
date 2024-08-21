
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
fs3 = frozenset([5, 6])

print("Copy of fs1:", fs1.copy())


print("Difference between fs1 and fs2:", fs1.difference(fs2))

print("Intersection of fs1 and fs2:", fs1.intersection(fs2))


print("Union of fs1 and fs2:", fs1.union(fs2))


print("Symmetric difference between fs1 and fs2:", fs1.symmetric_difference(fs2))

print("Is fs3 a subset of fs2?", fs3.issubset(fs2))

print("Is fs2 a superset of fs3?", fs2.issuperset(fs3))


print("Are fs1 and fs3 disjoint?", fs1.isdisjoint(fs3))


print("Does fs1 contain 2?", 2 in fs1)


print("Length of fs1:", len(fs1))


print("Elements in fs1:")
for elem in fs1:
    print(elem)


print("Hash of fs1:", hash(fs1))

print("String representation of fs1:", repr(fs1))
