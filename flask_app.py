from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from readData import readFilms
from insertData import addfilms
from updateData import updatefilms
from deleteData import deletefilm
from printOptions import optionsFilms


app = Flask(__name__)
app.config["DEBUG"] = True

# SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
#     username="joesasai90",
#     password="BobBobber!23",
#     hostname="joesasai90.mysql.pythonanywhere-services.com",
#     databasename="joesasai90$comments",
# )
# app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
# app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class Comment(db.Model):

#     __tablename__ = "comments"

#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(4096))

Comment=optionsFilms()

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        Comment=optionsFilms()
        return render_template("index.html", comments=Comment)

    if request.method == "POST":
        if "add" in request.form:
            data1 = request.form["Title"]
            data2 = request.form["Release"]
            data3 = request.form["Rating"]
            data4 = request.form["Duration"]
            data5 = request.form["Genre"]
            Comment=addfilms(data1, data2, data3, data4, data5)
        elif "read" in request.form:
            searchGenre = request.form["GenreRead"]
            Comment=readFilms(searchGenre)
            return render_template("index.html", comments=Comment)
        elif "update" in request.form:
            upData0 = request.form["FilmId"]
            upData1 = request.form["Title2"]
            upData2 = request.form["Release2"]
            upData3 = request.form["Rating2"]
            upData4 = request.form["Duration2"]
            upData5 = request.form["Genre2"]
            Comment=updatefilms(upData0, upData1, upData2, upData3, upData4, upData5)
        elif "del" in request.form:
            delData = request.form["deleteFilm"]
            deletefilm(delData)
            Comment=optionsFilms()
            return render_template("index.html", comments=Comment)
    return redirect(url_for('index'))


