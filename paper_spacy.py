import spacy

nlp = spacy.load("de_core_news_md")

with open("rieger.txt", encoding="utf-8") as file:
    text = file.read()

doc = nlp(text)

# Analyze syntax
print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

# Find named entities, phrases and concepts
for entity in doc.ents:
    print(entity.text, entity.label_)

file = open("paper_spacy.csv", "w", encoding="utf-8")
for entity in doc.ents:
    file.write(str(entity.text) + ",")
    file.write(str(entity.label_) + "\n")


