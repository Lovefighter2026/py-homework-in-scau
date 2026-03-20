paragraph = input("Enter a paragraph: ")
word_to_find = input("Enter the word to find: ")
word_to_replace = input("Enter the word to replace it with: ")
modified_paragraph=paragraph.replace('{word_to_find}','{word_to_replace}',100)

print("Modified paragraph:", modified_paragraph)
