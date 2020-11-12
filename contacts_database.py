import sqlite3

db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts(name, phone, email) VALUES('Tim', 6595, 'tim@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Brian', 1234, 'my@email.com')")

# In Python, there is no need to add a semicolon ';' at the end of sequel statements.
# They will still execute.

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")

print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone()) # will not grab another row bc there is only 2, returning: None
for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)
# cursor can't go back to previous records
# cursors don't store previous entries, making them efficiently fast

# print(cursor.fetchall())

# for row in cursor:
#     print(row)

cursor.close()
db.commit() # commiting the change, allowing for access of data beyond this file
db.close()