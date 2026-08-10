# for loop is used to repeat a block of code for a fixed number of times

# program 1
# print multiplication table

number = int(input("Enter a number to print table: "))

print("\nMultiplication Table of", number)

for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)


# program 2
# find sum of numbers in a list

numbers = [10, 20, 30, 40, 50]
total = 0

for num in numbers:
    total = total + num

print("\nNumbers:", numbers)
print("Total Sum:", total)


# program 3
# count vowels in a string

text = input("\nEnter a word or sentence: ")

vowel_count = 0

for letter in text.lower():
    if letter in "aeiou":
        vowel_count += 1

print("Total vowels:", vowel_count)