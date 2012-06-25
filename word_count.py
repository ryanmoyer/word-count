# Word Count
# Author: Ryan Moyer

print 'Word Count'
print 'Tells how many words are in a document.'
input_file_name = raw_input('Please enter the name of the document you would like to words counted: ')
with open(input_file_name) as input_file:
    for line in input_file:
        for word in line.split():
            print word
