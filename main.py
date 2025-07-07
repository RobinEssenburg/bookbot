from stats import get_word_count
from stats import get_character_count
from stats import sorting_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)
    words = get_word_count(book)
    characters = get_character_count(book)
    sorted_characters = sorting_dictionary(characters)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path}")
    print(f"----------- Word Count ----------\nFound {words} total words\n--------- Character Count -------")
    for entry in sorted_characters:
        print(f"{entry["char"]}: {entry["num"]}")
    print("============= END ===============")

main()