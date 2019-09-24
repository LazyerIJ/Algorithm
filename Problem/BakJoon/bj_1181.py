import operator
import sys

input_len = int(sys.stdin.readline())
len_word_dict = {}
len_flag=0
same_len_words=[]

for step in range(input_len):
    input_word = sys.stdin.readline().strip()
    len_word_dict.update({input_word:len(input_word)})

len_word_dict_sorted = sorted(len_word_dict.items(), 
                              key  = operator.itemgetter(1))

for word in len_word_dict_sorted:

    if word[1] != len_flag:
        for t1 in sorted(same_len_words):
            print(t1)
        same_len_words=[]
    same_len_words.append(word[0])
    len_flag=word[1]

for t1 in sorted(same_len_words):
    print(t1)


