import _sqlite3

connection = _sqlite3.connect("my_database.sqlite")
cursor = connection.cursor()

sqlcommand = """
PRAGMA encoding = UTF8; 
"""
cursor.execute(sqlcommand)


sqlcommand1 = """CREATE TABLE IF NOT EXISTS rdfdump (
eigene_id integer PRIMARY KEY,
autor text,
titel text,
keywords text,
viaf varchar

);"""
cursor.execute(sqlcommand1)

variable1 = "bla"
sql_command2 = """INSERT INTO rdfdump (eigene_id, autor, titel, keywords, viaf)
    VALUES (NULL, "diderot", "jaques", "%s", "http.irgendwas");"""

liste = ["dies", "ist", "eine", "Liste"]
bla = "jop"
for i in liste:
    cursor.execute("""INSERT INTO rdfdump (eigene_id, autor, titel, keywords, viaf)
        VALUES (NULL, ?, ?, ?, ?)""", (bla, bla, bla, bla))


connection.commit()

connection.close()