import sqlite3  # import sqlite library



"create a variable conn and pass the sqlite connect method to it "

# conn = sqlite3.connect("folderpth/folderpath/fileName.dbExtension")

# create db if it does not exists

conn = sqlite3.connect("/home/joesasai90/mysite/data/filmflix.db")

# cursor

cursor = conn.cursor()

