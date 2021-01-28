
import sqlite3

conn = sqlite3.connect('test2.db')

# Creating a table with an ID primary key and a key with a string value
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_FileName TEXT)")
    conn.commit()
conn.close()


conn = sqlite3.connect('test2.db')

# Our tuple we need to sort through
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf','myPhoto.jpg')

# How we are sorting through our list to find any files with the '.txt' ending
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            # The value will be one name out of the tuple therefore the (x,)
            cur.execute("INSERT INTO tbl_files (col_FileName) VALUES (?)", (x,))
            print(x)
conn.close()
