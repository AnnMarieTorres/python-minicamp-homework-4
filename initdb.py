import sqlite3

conn = sqlite3.connect('database.db')
print 'Opened database successfully';

conn.execute('CREATE TABLE movies(name TEXT, genre TEXT)')
print 'Table Created Successfully';

conn.close()