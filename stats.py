from collections import Counter


def get_num_words(text):
    words = text.split()
    return len(words)


def count_chars(text):
    return Counter(text.lower())


def order_dict(chars):
    dict_list = []
    for k, v in chars.items():
        dict_list.append({"char": k, "num": v})
    dict_list.sort(key=lambda x: x["num"], reverse=True)
    return dict_list