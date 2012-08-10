def count_words_in_file(file_name):
    word_count = {}
    with open(file_name) as input_file:
        for line in input_file:
            for word in line.split():
                if word in word_count:
                    word_count[word] = word_count[word] + 1
                else:
                    word_count[word] = 1
    return word_count
