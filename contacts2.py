import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'anotherupdate@updateemail.com'
phone = input('Please enter the phone number ')

# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
# placeholders are better than using string formatting.
# don't do this however if dealing with user input for security purposes
# use ? mark when you want an actual value to be inputted
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone)) # .executescript gets rid of the database
print("{} rows updated".format(update_cursor.rowcount)) # updating rows where contacts.phone = 1234
# 1 row was updated

print("Are connections the same: {}".format(update_cursor.connection == db))

update_cursor.connection.commit() # must commit code
update_cursor.close()

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

db.close()

# writing code 1:10 reading code