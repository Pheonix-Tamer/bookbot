file_path = "books/frankenstein.txt"

def main():
    book = get_file_data()
    num_words = get_num_words(book)
    num_chars = number_of_char(book)
    chars_lst = chars_dict_to_list(num_chars)
    chars_lst.sort(reverse=True, key=sort_on)
    print_report(num_words, chars_lst)
    

def get_num_words(text):
    words = text.split()
    return len(words)


def get_file_data():
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def number_of_char(text):
    chars = {}
    text = text.lower()
    for char in text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars


def chars_dict_to_list(chars):
    new_lst = []
    for item in chars:
        # print(item)
        c = {"name": item, "num": chars[item]}
        if item.isalpha():
            new_lst.append(c)
    return new_lst


def sort_on(c):
    return c["num"]


def print_report(word_count, char_count):
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in char_count:
        c = char["name"]
        n = char["num"]
        print(f"The '{c}' character was found {n} times")
    print("--- End Report ---")


main()
