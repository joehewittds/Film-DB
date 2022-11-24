from sqlConnect import *


def readFilms(genreField):

    genreField = genreField.strip()

    # Retrieve the inserted songs
    cursor.execute(f"SELECT * FROM tblfilms WHERE genre='{genreField}'")  # select all songs
    row = cursor.fetchall()  # fetch all songs that was selected above
    # iterate through all the fetched records
    # for record in row:
    #     print(record)
    return row

if __name__ == "__main__":
    readFilms()
