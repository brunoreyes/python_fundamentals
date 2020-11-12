# create a file by
# 1. Going to a terminal: 2. sqlite3 nameofdatabase.db
# 2. for access to list of commands: .help
# 3. turn display of headers on with: .headers on
# 4. create a table with column headers: create table contacts ( name text, phone integer, email text);
# 5. instert data into table: insert into contacts (name, phone, email) values('Tim',65478,'tim@gmail.com');
# select all from table: SELECT * from tablename
# select specific colums from table: SELECT name, phone, email FROM tablename
# recall to use the appropriate type when inserting data or selecting data
# to make a backup of the table: .backup testbackupdbname
# to go back: .restore testbackupdbname

# UPDATE contacts SET email="steve@hisemail.com" WHERE name = "Steve";

# SELECT phone, email FROM contacts WHERE name="Brian";
# DELETE FROM contacts WHERE phone=1234;

# show all tables within a database: .tables
# .schema  shows the structure of the database and all the tables within it: .schema
# .dump: gets all queries that were used to create and add data to a table

# you can open up a db from your local device like this: sqlite3 localfilename.db
# sqlite> .schema
# CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
# CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
# CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);

# SELECT * FROM artists WHERE _id=133;
# SELECT name FROM albums WHERE _id=167;

#  ignoring case sensitivity : SLECT * FROM albums ORDER BY name COLLATE NOCASE;
# SELECT * FROM albums ORDER BY name COLLATE NOCASE DESC;
# SELECT * FROM albums ORDER BY artist, name COLLATE NOCASE DESC; sorting first by 'artist id' then 'name'
# SELECT * FROM songs ORDER BY songs.album, songs.track;

# JOINS allow for greater flexibility and manipulation of data
# SELECT songs.track, songs,title, albums.name FROM songs JOIN albums ON songs.album = albums._id;
# Always specify the table name

# SELECT songs.track, songs.title. albums.name FROM songs INNER JOIN albums ON songs.albums = albums._id;

# SELECT songs.track, songs.title. albums.name FROM songs INNER JOIN albums ON songs.albums = albums._id
# ORDER BY albums.name, songs.track;

# SELECT albums.name, songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id

# JOIN returns all rows from tables where the key record of one table is equal to the key records of
# another table.

# INNER JOIN selects all rows from both participating tables as long as there is
# a match between the columns.

# Creating a list of all artists, their albums, in alphabetical order of artist
# SELECT artists.name, albums.name FROM artists INNER JOIN albums ON albums.artist = artists._id ORDER BY artists.name;


# SELECT artists.name, albums.name, songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artist ON albums.artist = artist._id
# ORDER BY artists.name, albums.name, songs.track;

# SELECT artists.name, albums.name, songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artist ON albums.artist = artist._id
# WHERE albums._id = 19
# ORDER BY artists.name, albums.name, songs.track

# SELECT artists.name, albums.name, songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artist ON albums.artist = artist._id
# WHERE songs.title LIKE '%doctor%' #here we can find any albums that contain the word doctor
# ORDER BY artists.name, albums.name, songs.track;

# Wildcard is %, *, ? and is a character is used to substitute one or more characters in a string.
# for example: WHERE songs.title LIKE 'car%' # car is at the beginning this time


# Views can restrict columns that are shown
# CREATE VIEW artist_list AS
# SELECT artists.name, albums.name, songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artist ON albums.artist = artist._id
# ORDER BY artists.name, albums.name, songs.track;

# SELECT * FROM artist_list;

# CREATE VIEW album_list AS
# SELECT name FROM albums
# ORDER BY name;

# SELECT * FROM album_list

# to delete view: DROP VIEW album_list
# to delete view: DROP TABLE album_list


# SELECT * FROM artist_list WHERE name LIKE "jeffersion%"

# CREATE VIEW album_list AS
# SELECT name FROM albums
# ORDER BY name collate nocase; # ignoring case and going by alphabetic order

# creating a backup of the database: .backup music-backup2
# DELETE FROM songs WHERE track < 50;

# SELECT * FROM songs WHERE track = 71;
# SLECT  count(*) FROM artists;
# .restore music-backup2
# 
# SELECT count(*) FROM artists;
# 
# SELECT songs
# 
# SELECT songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# WHERE albums.name = 'Forbidden'; #here we can find any albums that contain the word doctor
# 
# SELECT songs.track, songs.track, songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# WHERE albums.name = 'Forbidden'
# ORDER BY songs.track;
# 
# 
# SELECT songs.track, songs.title  FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Deep Purple';
# 
# UPDATE artists SET name = 'One Kitten' WHERE name = 'Mehitabel';
#
#
# 
# SELECT songs.title FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Aerosmith'
# ORDER BY songs.title ASC;
# 
#
# SELECT count(*) FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Aerosmith';
#
# SELECT DISTINCT gets rid of duplicate entries like songs or numbers
# SELECT DISTINCT songs.title FROM songs 
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Aerosmith'
# ORDER BY songs.title ASC;
#
# gets the unique count of items within a column within a table
# SELECT COUNT (DISTINCT tableName.columnName)
# SELECT COUNT (DISTINCT songs.title) FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Aerosmith';
# 
#
# # SELECT COUNT (DISTINCT tableName.columnName)
# SELECT COUNT (DISTINCT albums.name) FROM songs
# INNER JOIN albums ON songs.album = albums._id
# INNER JOIN artists ON albums.artist = artists._id
# WHERE artists.name = 'Aerosmith';
#
#
#
#
# 
#
# 
#
# 




