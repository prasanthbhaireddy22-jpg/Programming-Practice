# sequence operations are common operations performed on lists and tuples

# program 1
# length, indexing and slicing

numbers = [10, 20, 30, 40, 50]

print("List:", numbers)
print("Length of list:", len(numbers))
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Sliced elements:", numbers[1:4])


# program 2
# membership and repetition

fruits = ("apple", "banana", "mango")

print("\nTuple:", fruits)

check_item = input("Enter fruit name to check: ")

if check_item in fruits:
    print(check_item, "is available")
else:
    print(check_item, "is not available")

print("Repeated Tuple:", fruits * 2)


# program 3
# concatenation and iteration

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = list1 + list2

print("\nCombined List:", combined_list)

print("Elements in combined list:")
for item in combined_list:
    print(item)