import sqlite3


conn = sqlite3.connect('databases/org-db.sqlite')
cur = conn.cursor()

# start with a clean slate
cur.execute('DROP TABLE IF EXISTS Counts')

# create a new table
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

# open the txt file for reading
fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From:'): continue
    pieces = line.split('@')
    org = pieces[1].rstrip()
    # print(org)
    cur.execute('SELECT count FROM Counts WHERE org= ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
        VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
conn.commit()  # writes the info out to disk

# in general, use the '?' to avoid SQL injection in online applications
# here it is a placeholder to be populated by a tuple (email,)
# UPDATE is a single atomic operation (better than read then write approach)

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])  # the row is returned as a tuple

cur.close()




