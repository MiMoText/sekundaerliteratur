import paper_nltk
import langdetect
from langdetect import detect

text = "Candide ist das meistgelesene Werk Voltaires und war es wohl schon zu Lebzeiten des Autors. Als es 1759 in Genf erstmals im Druck erschien, wurde es zwar sofort verboten, aber doch nur mit dem Ergebnis, daß es im gleichen Jahr noch dreizehn Neuauflagen erlebte."
print(type(text))


tokens = paper_nltk.word_tokenize(text)
print(type(tokens))
detect(text)
detect(tokens[0])

for i in range(len(tokens)):
    print(tokens[i])
    print(type(tokens[i]))

for i in range(len(tokens)):
    detect(tokens[i])
    

#tagged = nltk.pos_tag(tokens)
#print(tagged)

#entities = nltk.chunk.ne_chunk(tagged)
#print(entities)










