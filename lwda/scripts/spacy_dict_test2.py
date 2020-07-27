import nltk.tokenize
import spacy

nlp_de = spacy.load("de_core_news_md")

farben = {"blau": {"hellblau": "kornblumenblau", "dunkelblau": "ultramarin"}, "grün": {"hellgrün": "grasgrün", "dunkelgrün": "oliv"}}

beispieltext = "Dies ist ein Beispieltext."
# beispieltext = nltk.tokenize.word_tokenize(beispieltext)
print(beispieltext)
# doc = nlp_de(beispieltext)
for id, info in farben.items():
    print("Übergeordnete Farbe:", id)
    for key in info:
        print(key + ":", info[key])

dictofWords = dict.fromkeys(beispieltext)
print(dictofWords)

for key, value in dictofWords:
    if key == doc.ents:
        value  = key.lable

print(dictofWords)
