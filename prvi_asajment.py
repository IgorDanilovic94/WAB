import sqlite3
conn = sqlite3.connect("TestDB.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
   id_book INT PRIMARY KEY,
   title TEXT,
   year INT);
""")
conn.commit()

id_book=int(input("Unesite id knjige: "))
title=input("Unesite naziv knjige: ")
year=input("Unesite godinu izdavanja: ")
book = (id_book,title,year)
cursor.execute("INSERT INTO Books VALUES (?, ?, ?)", book)
conn.commit()

cursor.execute("SELECT * FROM Books;")
knjige = cursor.fetchall()
for book in knjige:
    print(book)
