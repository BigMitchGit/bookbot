from stats import get_num_words, get_num_chars, sort_dict
import sys


def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()

    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    num_chars = get_num_chars(contents)
    sorted = sort_dict(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted:
        print(f"{item["char"]}: {item["num"]}")

    print("============= END ===============")


main()
