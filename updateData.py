from sqlConnect import *
from readData import readFilms
import time


def updatefilms(idField, title, yearReleased, rating, duration, genre):

    # What field is ideal for updating a record in the films table and why ?

    # SongID     of the record to be updated

    # idField = input("Enter the filmID of the film to be updated: ")

    # Enter the name of the field(Title/Artist/Genre)

    # fieldName = input(

    #     "Which field would you like to update(Title, year released, guidance rating, duration, genre)? "

    # ).title()

    # Enter the value for the field(Title,Artist,Genre)

    # newFieldValue = input(f"Enter the new value for the field: {fieldName} ")

    # print(f"The new field value entered is {newFieldValue}")



    # add single quotes arround the new field value

    # name  = Anna,  now name = " ' " + Anna + " ' "  = 'Anna'

    # newFieldValue = "'" + newFieldValue + "'"

    # print(f"The new field value entered is {newFieldValue}")


    films = []
    films.append(title)  # append title
    films.append(yearReleased)  # append artist
    films.append(rating)  # append artist
    films.append(duration)  # append artist
    films.append(genre)  # append genre
    # Update the films table

    "UPDATE films SET Title/Artist/Genre = newFieldValue(Dance/MJ/Pop) WHERE SongID = 1/2/3... "

    cursor.execute(f"UPDATE tblfilms SET title  = '{films[0]}', yearReleased  = {films[1]}, rating  = '{films[2]}', duration  = {films[3]}, genre  = '{films[4]}' WHERE filmID = {idField}")

    conn.commit()



    # returns the id of the song to be updated

    # print(f"record {idField} Updated in the films table")

    time.sleep(3)

    # call/invoke the readfilms from readData

    # readFilms()



if __name__ == "__main__":
    updatefilms()