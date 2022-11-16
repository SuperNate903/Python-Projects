import sqlite3

fileList = ("information.docx","Hello.txt","myImage.png", \
            "myMovie.mpg","World.txt","data.pdf","myPhoto.jpg")

conn = sqlite3.connect("py_database.db")

with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS tbl_files")
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
    )")
    
    for file in fileList:
        if file.endswith(".txt"):
            cur.execute("INSERT INTO tbl_files(col_file) VALUES (?)", \
                (file,))
    
    cur.execute("SELECT * FROM tbl_files")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "File: {}\n".format(item)
        print(msg)
    conn.commit()
conn.close()
