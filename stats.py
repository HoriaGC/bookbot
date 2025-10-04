def word_counter(file):
    with open(file) as f:
        source_txt = f.read()
    countables = source_txt.split()
    num_words = 0
    for i in countables:
        num_words += 1
    print(f"Found {num_words} total words") 


def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
     


def char_counter(file):
    with open(file) as f:
        source_txt = f.read()
    countables = source_txt.split()
    num_words = 0
    charz = {}
    for i in countables:
        num_words += 1
    for i in source_txt.lower():
        if i in charz:
            charz[i] += 1
        else:
            charz[i] = 1
    return charz, num_words
    # print(f"Found {num_words} total words") 
    # print(charz)


def reporter(file):
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