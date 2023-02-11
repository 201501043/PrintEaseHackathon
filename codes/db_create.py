import sqlite3

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('users.db')

# Create a cursor
cursor = conn.cursor()

# Execute a SQL command to create the table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL,
  password TEXT NOT NULL,
  email TEXT NOT NULL,
  message TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS TimeTable (
  Year TEXT NOT NULL,
  Dept TEXT NOT NULL,
  Section TEXT NOT NULL,
  loc TEXT,ID TEXT
)
''')
# cursor.execute("Drop table timetable")
cursor.execute("Select loc, id from TimeTable")
res = cursor.fetchall();
for i in range(len(res)):
    print(res[i])
# Commit the changes and close the connection
conn.commit()
conn.close()
