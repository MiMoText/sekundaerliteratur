from lwda.scripts.my_nltk import word_tokenize


with open("../data_out/keywords_sortiert.CSV", encoding="ansi") as file:
    data = file.read()

print(data)
data = word_tokenize(data)
erzaehlperspektiven = ["1e personne", "3e personne", "lettre"]
orte = []
personen = ["le", "la", "Madame", "Monsieur", "M."]
gattung = ["intrigue", "aventure"]
attitude = ["sensibilité", "mélancolie", "ton satirique"]
zuordnungswörter = ["1e personne", "3e personne", "lettre", "le", "la", "Madame", "Monsieur", "M.", "intrigue", "aventure", "sensibilité", "mélancolie", "ton satirique"]
zuordnung_zu_erzaehlperspektiven = []
zuordnung_zu_personen = []
zuordnung_zu_gattung = []
zuordnung_zu_attitude = []
ohne_zuordnung = []

for j in range(len(data)):
    if j not in zuordnungswörter:
        ohne_zuordnung.append(data[j])

for i in range(len(erzaehlperspektiven)):
    if erzaehlperspektiven[i] in data:
        zuordnung_zu_erzaehlperspektiven.append(erzaehlperspektiven[i])
    else: ohne_zuordnung.append(erzaehlperspektiven[i])
print(zuordnung_zu_erzaehlperspektiven)

for i in range(len(personen)):
    if personen[i] in data:
        zuordnung_zu_personen.append(personen[i])
    else: ohne_zuordnung.append(personen[i])
print(zuordnung_zu_personen)

for i in range(len(gattung)):
    if gattung[i] in data:
        zuordnung_zu_gattung.append(gattung[i])
    else:ohne_zuordnung.append(gattung[i])
print(zuordnung_zu_gattung)

for i in range(len(attitude)):
    if attitude[i] in data:
        zuordnung_zu_attitude.append(attitude[i])
    else: ohne_zuordnung.append(attitude[i])
print(zuordnung_zu_attitude)

print("ohne zuordnung")
print(ohne_zuordnung)

"""


    
    
    # data tokenisieren, damit ganze wörter und nicht einzelne zeichen
     ACHTUNG tokenizer reißt wörter, die zusammengehören auseinander wie jeune homme, bessere lösung wohl tatsächlich ausnahmsweise auf regex-basis
  # besser einfach als csv exportieren und in excel machen  
  # nicht vergessen am ende den ganzen eintrag auszugeben, nicht nur dne teil der gemacht hat (erledigt in tokenregex_test.py, muss noch in gesamtskript integeriert werden
  so, stand 24.03. abends: soweit ungefähr richtig, jetzt nochmal konzentration auf den rdf-export in korrekter form
  +
  falls notwendig Bereinigungsschritte
"""






