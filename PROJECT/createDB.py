import sqlite3
from sqlite3 import OperationalError

# Connect to SQLite database (creates the database file if it doesn't exist)
conn = sqlite3.connect("Local_Championship.db")
c = conn.cursor()

# Open and read the file as a single buffer
fd = open('schemas.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

# Execute every command from the input file
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        c.execute(command)
    except OperationalError:
        print("Command skipped: ")

conn.commit()
conn.close()
