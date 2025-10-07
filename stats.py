def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list



#  def word_counter(file):
#     with open(file) as f:
#         source_txt = f.read()
#     countables = source_txt.split()
#     num_words = 0
#     for i in countables:
#         num_words += 1
#     print(f"Found {num_words} total words") 


# def get_book_text(file):
#     with open(file) as f:
#         file_contents = f.read() 


# def char_counter(file):
#     with open(file) as f:
#         source_txt = f.read()
#     countables = source_txt.split()
#     num_words = 0
#     charz = {}
#     for i in countables:
#         num_words += 1
#     for i in source_txt.lower():
#         if i in charz:
#             charz[i] += 1
#         else:
#             charz[i] = 1
#     return charz, num_words
#     # print(f"Found {num_words} total words") 
#     # print(charz)


# def reporter(file):
    char_dict, num_words = char_counter(file)
    list_of_letters = []
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at{file}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for i in char_dict:
        list_of_letters.append(i)
        list_of_letters.sort(reverse=True)
        print(list_of_letters[i])