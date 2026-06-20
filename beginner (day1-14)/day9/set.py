set1 = {1, 2, 3, 4}
set2 = {2, 3, 4, 5, 6}

set1.add(5)
print(set1)

set1.remove(5)
print(set1)

set2.clear()      # Empty the set
print(set2)

print(set1.pop()) # Removes and returns an arbitrary element

set2 = {2, 3, 4, 5, 6}

print(set1.union(set2))         # All unique elements
print(set1.intersection(set2))  # Common elements 