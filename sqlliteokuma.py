import sqlite3
db = sqlite3.connect(':memory:')
c = db.cursor()
c.execute('''CREATE TABLE kullanici(id INTEGER PRIMARY KEY, ad TEXT, telefon TEXT)''')
kullanicilar = [
    ('Ahmet', '5555544554'), 
    ('Hayri', '5567544554'), 
    ('Hüseyin', '5578944554'), 
    ('Recep',' 5555588754')
]
 
c.executemany('''INSERT INTO kullanici(ad, telefon) VALUES(?,?)''', kullanicilar)
db.commit()
 

c.execute('''SELECT * FROM kullanici''')
for satir in c:
    print(satir)
 
db.close()