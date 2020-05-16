from __future__ import division
import nltk
import re
import pprint


with open("../data_in/rieger.txt", encoding="utf-8") as file:
    data = file.read()
tokens = nltk.tokenize.word_tokenize(data)
# es gibt noch ungefähr zehntausend andere tokenizer in nltk.tokenize
print(tokens)

sentences = nltk.sent_tokenize(data)

pos_tagged = nltk.pos_tag(tokens)

ne_tagged = nltk.ne_chunk(pos_tagged)
print(ne_tagged)

file = open("../data_out/paper_nltk.csv", "w", encoding="utf-8")

for word in ne_tagged:
    file.write(str(word) + "\n")
