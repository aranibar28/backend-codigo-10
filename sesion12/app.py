from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask import render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/movies"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/movies")
def get_movies():
    results = db.session.execute("SELECT * FROM cartelera")
    return render_template("index.html", rows = results)