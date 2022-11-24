from sqlConnect import *
import time

# create a subroutine to add films to the films table
def addfilms(title, yearReleased, rating, duration, genre):
    # create an empty list
    films = []

    # title = input("Enter films Title: ")
    # yearReleased = input("Enter year released(yyyy): ")
    # rating = input("Enter film rating(eg. PG, R, G): ")
    # duration = input("Enter film duration(minutes): ")
    # genre = input("Enter film Genre: ")


    # append data enterd by user to song list
    "films.SongID is set to auto increment and would be added in automatically"

    films.append(title)  # append title
    films.append(yearReleased)  # append artist
    films.append(rating)  # append artist
    films.append(duration)  # append artist
    films.append(genre)  # append genre



    # insert data from films list into the films table

    cursor.execute("INSERT INTO tblfilms VALUES(NULL, ?,?,?,?,?)", films)

    conn.commit()  # save changes permanently to films table



    # print(f"The film {title} added to films table") # returns the title of the song to be added

    time.sleep(3)

    # retrieve the entire record of the song added to the database

    getData = cursor.execute("SELECT * FROM tblfilms") # select all films
    # print(getData)
    row = getData.fetchall() #fetch all films that was selected above

    # iterate through all the fetched records

    # for record in row:
    #  print(record)

if __name__ == "__main__":
    addfilms()
