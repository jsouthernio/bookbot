with open("books/frankenstein.txt") as f:
    file_contents = f.read()

words = file_contents.split()

char_count = {}
for word in words:
    word = word.lower()
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

count_list = list(char_count.items())
char_list = []
for item in count_list:
    if item[0].isalpha():
        char_list.append(item)
char_list.sort(key = lambda i:i[1], reverse = True)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(words)} words found in the document")
print()
for item in char_list:
    print(f"The '{item[0]}' character was found {item[1]} times")
print("--- End report ---")