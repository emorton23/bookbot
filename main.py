from stats import word_count, char_count, sorted_char_count
import sys

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Use the second argument as the book file path
    book_path = sys.argv[1]

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)

    print(f"Found {word_count(book_text)} total words")
    
    character_counts = char_count(book_text)
    sorted_counts = sorted_char_count(character_counts)
    
    print("Character Frequency Report:")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['num']}")

if __name__ == "__main__":
    main()