from stats import count_words, character_count, sort_on, sort_char
import sys


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_count = character_count(text)
    sorted = sort_char(char_count)
    print(f"============BOOKBOT============ \n Analyzing book found at {path}... \n ------------ Word Count------------ \n Found {num_words} total words \n --------- Character Count -----")
    for item in sorted:
        print(f"{item['char']}: {item['num']}")


main()