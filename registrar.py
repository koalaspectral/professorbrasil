import sqlite3

banco = sqlite3.connect('main.db')

cursor = banco.cursor()

cursor.execute("INSERT INTO bagmons VALUES(2,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(3,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(4,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(5,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(6,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(7,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(8,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(9,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(10,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(11,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(12,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(13,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(14,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(15,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(16,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(17,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(18,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(19,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(20,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(21,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(22,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(23,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(24,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(25,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(26,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(27,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(28,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(29,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(30,'','',,,'vazio','vazio','vazio','vazio','vazio')")
cursor.execute("INSERT INTO bagmons VALUES(31,'','',,,'vazio','vazio','vazio','vazio','vazio')")


"""cursor.execute("SELECT * FROM bagmons")

print(cursor.fetchall())
"""
banco.commit()