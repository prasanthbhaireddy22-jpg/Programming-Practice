# sets store unique values and do not allow duplicates

# program 1
# creating a set and adding elements

numbers = {10, 20, 30, 40}

print("Original Set:", numbers)

numbers.add(50)
numbers.add(60)

print("After Adding Elements:", numbers)


# program 2
# removing elements from a set

fruits = {"apple", "banana", "mango", "orange"}

print("\nOriginal Set:", fruits)

fruits.remove("banana")

print("After Removing Banana:", fruits)

fruits.discard("grapes")  # no error if item not found

print("After Discard Operation:", fruits)


# program 3
# set operations (union and intersection)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))