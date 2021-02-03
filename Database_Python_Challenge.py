import sqlite3

rosterValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'''not",'Mangalore', -5))

with sqlite3.connect('db_test1.db') as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS Roster(Name TEXT, Species TEXT, IQ INT)")
    c.executemany("INSERT INTO Roster VALUES(?, ?, ?)",
                  rosterValues)
    c.execute("UPDATE Roster SET Species = 'Human' WHERE Species = 'Meat Popsicle'")

    # Select all names and IQ of everyone in the table who is classified as human
    c.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human';")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)
