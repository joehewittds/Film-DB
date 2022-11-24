from sqlConnect import *
from readData import readFilms
import time




def deletefilm(idField):

    # What field is ideal for deleting a record in the films table and why ?

    # filmID of the record to be updated

    # idField = input("Enter the filmID of the film to be deleted: ")


    cursor.execute(f"DELETE FROM tblfilms WHERE filmID={idField}")

    conn.commit()

    # returns the id of the deleted film

    # print(f"Record {idField} deleted from the films table")

    # time.sleep(3)

    # call/invoke the readfilms from readData

    # readFilms()



if __name__ == "__main__":
    deletefilm()