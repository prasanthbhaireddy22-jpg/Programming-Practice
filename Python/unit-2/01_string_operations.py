# string operations in python

# program 1
# finding length, uppercase and lowercase

text = input("Enter a text: ")

print("\nOriginal Text:", text)
print("Length of text:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())


# program 2
# checking first and last character

word = input("\nEnter a word: ")

print("First character:", word[0])
print("Last character:", word[-1])
print("Reversed word:", word[::-1])


# program 3
# counting vowels and spaces

sentence = input("\nEnter a sentence: ")

vowel_count = 0
space_count = 0

for letter in sentence.lower():
    if letter in "aeiou":
        vowel_count += 1
    if letter == " ":
        space_count += 1

print("\nTotal vowels:", vowel_count)
print("Total spaces:", space_count)