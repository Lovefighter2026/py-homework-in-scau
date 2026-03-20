text = input("Enter a string: ")
text = text.lower()
letter_count = {}
for char in text:
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
print("Letter frequencies:")
for letter in sorted(letter_count.keys()):
    print(f"{letter}: {letter_count[letter]}")
