# this txt file with all words will be converted to a list
a_file = open('word.txt', 'r')
word_list = []

for line in a_file:
    line = line.strip()
    word_list. append(line)

a_file.close()