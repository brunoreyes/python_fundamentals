import sqlite3

conn = sqlite3.connect("contacts.sqlite")
name = input('Please enter a name ')

for row in conn.execute("SELECT * FROM contacts WHERE contacts.name LIKE ?", (name,)):
    print(row)


conn.close()