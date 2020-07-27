import nltk
# nltk.download("punkt")
with open("../data_in/richtig.txt", encoding="utf-8") as file:
    data = file.read()

tokens = nltk.tokenize.word_tokenize(data)

file = open("../data_out/richtig.csv", "w", encoding="utf-8")

for word in tokens:
    file.write(str(word) + "\n")