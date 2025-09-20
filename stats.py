def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    char_count = dict()
    lower_case = text.lower()
    for char in lower_case:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] = char_count[char] + 1
    return char_count

def sort_on(item):
    return item["num"]

def sort_char(character_count):
    list_char = []
    for k, v in character_count.items():
        if k.isalpha():
            list_char.append({"char": k , "num" : v})
    list_char.sort(reverse=True, key=sort_on)
    return list_char

