from collections import defaultdict

def count_words_in_file(file_name):
    word_count = defaultdict(int)
    with open(file_name) as input_file:
        for line in input_file:
            for word in line.split():
                word_count[word] += 1
    return word_count
