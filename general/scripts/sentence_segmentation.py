import nltk
import codecs
import glob
import os

# Dieses Skript liest alle txt-Files aus data_in ein, bestimmt die Satzgrenzen
# und schreibt den so segmentierten Text in data_out.
# Trennzeichen für Sätze ist \n , kann aber nach Bedarf geändert werden.

filelist = glob.glob("../data_in/*.txt")

for file in filelist:
    try:
        f = open(file, encoding="utf-8")
    except:
        print("File not found or not readable.")
        continue

    full_text = f.read()
    f.close()

    sent_tok = nltk.sent_tokenize(full_text, language="german")

    file_out = open("../data_out/" + str(os.path.basename(file)) + "file_out.txt", "w", encoding="utf-8")
    for sentence in sent_tok:
        file_out.writelines(sentence + "\n")

    file_out.close()
