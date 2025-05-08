def word_count(text):
    words = text.split()
    word_count= len(words)
    return word_count


def char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count


def sorted_char_count(char_count):
    sorted_list = sorted(
        [{"char": char, "num": count} for char, count in char_count.items()],
        key=lambda x: x["num"],
        reverse=True
    )
    return sorted_list

