# string methods are built-in functions used to perform operations on strings

# program 1
# using upper, lower, title

text = input("Enter a sentence: ")

print("\nOriginal Text:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())


# program 2
# using replace and count

sentence = input("\nEnter a sentence: ")

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

updated_sentence = sentence.replace(old_word, new_word)

print("\nUpdated Sentence:", updated_sentence)
print("Total spaces:", sentence.count(" "))


# program 3
# using startswith, endswith, find

email = input("\nEnter your email: ")

print("\nChecking Email Details")

if email.endswith(".com"):
    print("Valid .com email")
else:
    print("Not a .com email")

position = email.find("@")

if position != -1:
    print("Symbol @ found at position:", position)
else:
    print("@ symbol not found")