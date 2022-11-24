from sqlConnect import *


def optionsFilms():
    # Retrieve the inserted songs
    cursor.execute("SELECT * FROM tblfilms")  # select all songs
    row = cursor.fetchall()  # fetch all songs that was selected above
    # iterate through all the fetched records
    # for record in row:
    #     print(record)

    return(row)

# optionsFilms()






