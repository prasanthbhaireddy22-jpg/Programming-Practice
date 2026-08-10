# tuple() function is used to convert other data types into tuple

# program 1
# converting list to tuple

numbers_list = [10, 20, 30, 40, 50]

numbers_tuple = tuple(numbers_list)

print("Original List:", numbers_list)
print("Converted Tuple:", numbers_tuple)


# program 2
# converting string to tuple

text = input("Enter a word: ")

letters_tuple = tuple(text)

print("\nOriginal String:", text)
print("Tuple of characters:", letters_tuple)


# program 3
# converting user input into tuple

values = input("\nEnter values separated by space: ")

value_list = values.split()

value_tuple = tuple(value_list)

print("List:", value_list)
print("Tuple:", value_tuple)

print("\nDisplaying tuple elements:")
for item in value_tuple:
    print(item)