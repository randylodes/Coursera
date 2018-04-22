
# Relational Databases
# historical solution to intelligently use random access storage
# relationships between multiple tables of data
# can think of the DB as a service/abstraction/API layer
# CRUD - Create, Read, Update, Delete

# Application Developer and Database Administrator both contribute to the data model
# the schema makes best use of resources, storage, etc
#
# examples use SQLLite - very popular embedded lightweight db (and already present in python)
# Run these SQL statements in SQLLite GUI to get familiar with the basics:
#
# CREATE TABLE Users(
#	name VARCHAR(128),
#	email VARCHAR(128)
# )

# INSERT INTO Users (name, email) VALUES ('Chuck', 'csev@umich.edu');
# INSERT INTO Users (name, email) VALUES ('Colleen', 'cvl@umich.edu');
# INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
# INSERT INTO Users (name, email) VALUES ('Sally', 'a1@umich.edu');
# INSERT INTO Users (name, email) VALUES ('Ted', 'ted@umich.edu');
# INSERT INTO Users (name, email) VALUES ('Kristen', 'kf@umich.edu')

# DELETE FROM Users WHERE email='ted@umich.edu'

# UPDATE Users SET name='Charles' WHERE email='csev@umich.edu'

# SELECT * FROM Users WHERE email='csev@umich.edu'
# SELECT * FROM Users ORDER BY email
# SELECT * FROM Users ORDER BY name


# working with SQLLite DB in python code

import sqlite3

conn = sqlite3.connect('databases/emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

# we are going to use an earlier pice of code and store the values in a db instead of a dictionary

# fname = 'mbox-short.txt'
fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From:'): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email= ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
        VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
conn.commit()  # writes the info out to disk

# in general, use the '?' to avoid SQL injection in online applications
# here it is a placeholder to be populated by a tuple (email,)
# UPDATE is a single atomic operation (better than read then write approach)

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])  # the row is returned as a tuple

cur.close()




