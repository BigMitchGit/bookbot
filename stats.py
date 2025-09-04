def get_num_words(string):
    return len(string.split())


def get_num_chars(string):
    num_chars = {}

    for char in string.lower():
        if char not in num_chars:
            num_chars[char] = 1
        else:
            num_chars[char] += 1

    return num_chars


def sort_on(items):
    return items["num"]


def sort_dict(input):
    list_of_dicts = []

    for key, value in input.items():
        new_dict = {"char": key, "num": value}
        list_of_dicts.append(new_dict)

    return list_of_dicts
