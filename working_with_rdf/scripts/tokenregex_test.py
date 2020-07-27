from lwda.scripts.my_nltk import word_tokenize
import re


with open("../data_out/keywords_sortiert.CSV", encoding="ansi") as file:
    data = file.read()

print(data)
data = word_tokenize(data)

for i in range(len(data)):
    match = re.search(".*uli.*", data[i])
    print(match)

print(type(match))

# valid re.compile alle bezeichner
# oder zeichen nachschauen
# ziel ist alle elemente aus liste einzulesen
# maxsplit statt tokenize

valid = re.compile(".*uli.*")
print((valid.match("zulim")))
print((valid.match("affe")))

if valid.match("zulim"):
    print("jop")

liste = ["uli", "affe"]
for i in range(len(liste)):
    valid = re.compile(".*" + liste[i] + ".*")
    print((valid.match("zulim")))
    print((valid.match("affe")))

