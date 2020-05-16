liste = ["bla", "blub"]
liste2 = ["bla"]

print(type(liste[0]))
print(liste[0])

if liste[0] in liste2:
    print("jop")

if liste[1] in liste2:
    print("jop")
else:print("nö")

for i in range(len(liste)):
    if liste[i] in liste2:
        print("jop2")
    else: print("nö2")