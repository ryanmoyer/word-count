# Word Count
# Author: Ryan Moyer

print 'Word Count'
print 'Tells how many words are in a document.'
input_file_name = raw_input('Please enter the name of the document you would like to words counted: ')
# The with statement below does the same as the following code:
# input_file = open(input_file_name)
# print input_file.readline()
# input_file.close()
with open(input_file_name) as input_file:
    #print input_file.readline()
    for line in input_file:
        print line,
