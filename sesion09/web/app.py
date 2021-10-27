from flask import Flask
from flask import render_template
from flask import request
from flask_bootstrap import Bootstrap
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL(host="localhost", user="root", password="", db="mydb")

mysql.init_app(app)
conn = mysql.connect()
Bootstrap(app)

@app.route("/")
def index():
    return "<h1>Hello World!</h1>"

@app.route("/productos")
def get_productos():
    cursor = conn.cursor()

    query = request.args.get("q")

    sql = """
    SELECT p.idproducto, p.nombre, p.fechProduccion, p.descripcion, p.precio, c.nombre, m.nombre
    FROM producto AS p
    LEFT JOIN categoria AS c
    ON p.idcategoria = c.idcategoria
	LEFT JOIN marca AS m
    ON p.idmarca = m.idmarca
    """
    if query != None:
        sql = sql + f" WHERE p.nombre LIKE '%{query}%'"
        sql = sql + f" OR p.descripcion LIKE '%{query}%'"
        sql = sql + f" OR c.nombre LIKE '%{query}%'"
        sql = sql + f" OR m.nombre LIKE '%{query}%'"
        
    cursor.execute(sql)
    results = cursor.fetchall()

    return render_template("index.html", productos = results)
