import spacy
from spacy_langdetect import LanguageDetector
import csv
# Skript zur Tokenisierung, Sprachbestimmung, POS-Tagging, NER
# Ergebnisse: ziemlich gut. Erkennt auch ohne weiters Zutun mehrteilige Namen als Einheit
# Noch keine Unterscheidung in deutsche und französische Textteile, bis jetzt rein deutsch
# Info Spracherkennung: https://spacy.io/universe/project/spacy-langdetect


def preprocessing():

    # Deutsches und Französisches Sprachmodell laden
    nlp_de = spacy.load("de_core_news_md")
    nlp_fr = spacy.load("fr_core_news_sm")

    # Language Detector laden
    nlp_de.add_pipe(LanguageDetector(), name="language_detector", last=True)

    # Den zu untersuchenden Text öffen
    with open("../data_in/rieger.txt", encoding="utf-8") as file:
        text = file.read()
    # dem Text wird ein deutsches Sprachmodell zugewiesen
    # --> wird gleich geändert, erst Spracherkennung, dann Sprachmodell de oder fr

    doc = nlp_de(text)

    # Bestimmung der Sprache auf Dokumentebene
    print(doc._.language)

    dict_fr = {}
    dict_de = {}
    dict_all = {}
    dict_sonstiges = {}

    for sent in doc.sents:
        dict_all[sent] = sent._.language

    print(type(doc.sents))

    print(dict_all)

    for i in dict_all:
        if "fr" in dict_all[i]['language']:
            dict_fr[i] = dict_all[i]
        if "de" in dict_all[i]['language']:
            dict_de[i] = dict_all[i]
        else: dict_sonstiges = dict_all[i]
    # print(dict_fr)
    # print(dict_de)
    # print(dict_sonstiges)


    ##############################
    text_fr = []
    file = open("../data_out/spacy_lfr.txt", "w", encoding="utf-8")

    for j, k in dict_fr.items():
        print("Text:", j)
        file.write(str(j))
        for m in k:
            print(m + ":", k[m])

    file2 = open("../data_out/spacy_lde.txt", "w", encoding="utf-8")

    for n, o in dict_de.items():
        print("Text:", n)
        file2.write(str(n))

# ############## SpaCy deutsch ######################
# preprocessing()

nlp_de = spacy.load("de_core_news_md")
with open("../data_out/spacy_lde.txt", encoding="utf-8") as file:
    text = file.read()

doc = nlp_de(text)

# print([(X.text, X.label_) for X in doc.ents])
print([(X, X.ent_type_) for X in doc])

dictofWords = dict.fromkeys(doc)
token_entity_list = [(X, X.ent_type_) for X in doc]
for t in token_entity_list:
    if t[0] in dictofWords:
        dictofWords[t[0]] = t[1]

print(dictofWords)
dictofWords = dict(dictofWords)
file = csv.writer(open("../data_out/paper_spacy_exp3.csv", "w", encoding="utf-8"))
for key, val in dictofWords.items():
    file.writerow([key, val])

# ################ SpaCy Französisch ##############################

nlp_fr = spacy.load("fr_core_news_sm")
with open("../data_out/spacy_lfr.txt", encoding="utf-8") as file:
    text = file.read()

doc = nlp_fr(text)

# print([(X.text, X.label_) for X in doc.ents])
print([(X, X.ent_type_) for X in doc])

dictofWords = dict.fromkeys(doc)
token_entity_list = [(X, X.ent_type_) for X in doc]
for t in token_entity_list:
    if t[0] in dictofWords:
        dictofWords[t[0]] = t[1]

print(dictofWords)
dictofWords = dict(dictofWords)
file = csv.writer(open("../data_out/paper_spacy_fr.csv", "w", encoding="utf-8"))
for key, val in dictofWords.items():
    file.writerow([key, val])