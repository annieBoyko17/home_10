import sqlite3
connection = sqlite3.connect("it_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-3');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-2');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-1');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-1.2');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-2');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('0');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-1.7');")
cur.execute("INSERT INTO temperature_table (temperature) VALUES ('-3.2');")
connection.commit()
connection.close()

