d = open("abfrage.txt", "w", encoding="utf-8")

liste = [["Eintrag00", "Eintrag01"], ["Eintrag10", "Eintrag11"]]

for i in range(len(liste)):
    #d.writelines(str(liste[i]))

    for j in range(len(liste)):
        d.writelines(str(liste[i][j]))
        d.write(";")
    d.write("\n")