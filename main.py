import sys
from stats import get_num_words, count_chars, order_dict


def get_book_text(filepath):
    content = ""
    with open(filepath) as f:
        content = f.read()
    return content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    res = get_book_text(filepath)
    num = get_num_words(res)
    counter = count_chars(res)
    list_dicts = order_dict(counter)
    print(f"""
    ============ BOOKBOT ============
    Analyzing book at: {filepath}
    ----------- Word Count ----------
    Found {num} total words
    --------- Character Count -------
    """.rstrip())
    for l in list_dicts:
        if l['char'].isalpha():
            print(f"{l['char']}: {l['num']}")
    print('============= END ===============')

main()