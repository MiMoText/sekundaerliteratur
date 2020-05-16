import paper_nltk

with open("rieger.txt", encoding="utf-8") as file:
    data = file.read()

tokens = paper_nltk.word_tokenize(data)