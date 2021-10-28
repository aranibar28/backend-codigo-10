# Python

### 🖥️ Session 1 
- Operadores
- Condicionales
- Bucles
----------------------------
### 🖥️ Session 2
- Estructuras de control
- Colecciones
- Funciones
----------------------------
### 🖥️ Session 3
> Instalar y activar entorno virtual : 

    python -m venv env1
    cd sesion3/web/env1
    . Scripts/activate

> Instalar libreria Pillow para manipular imágenes : 

    pip install Pillow 

----------------------------

### 🖥️ Session 4
- Programación Orientada a Objetos (POO)

----------------------------

### 🖥️ Session 5
- Encampsulamiento
- Métodos mágicos

----------------------------
### 🖥️ Session 6
> Instalar y activar entorno virtual : 

    python -m venv env2
    cd sesion6/web/env2
    . Scripts/activate

>  Instalar Flask :

    pip install Flask

----------------------------
### 🖥️ Session 7
- Render Templates
- Jinja 3.0.x

> Instalar y activar entorno virtual : 

    python -m venv env3
    cd sesion6/web/env3
    . Scripts/activate

>  Instalar Flask :

    pip install Flask

>  Instalar Pillow :

    pip install Pillow 

----------------------------

### 🖥️ Session 8
- Flask Bootstrap
- Flask con Colecciones
- Flask con Librerias

> Instalar y activar entorno virtual : 

    python -m venv env4
    cd sesion8/web/env4
    . Scripts/activate

>  Instalar Flask :

    pip install Flask

>  Instalar Flask Bootstrap

    pip install flask-bootstrap

----------------------------

### 🖥️ Session 9
- Lenguaje de consulta T-SQL
- Flask y MSQL

>  Instalar Flask :

    pip install Flask

>  Instalar Mysql :

    pip install flask-mysql

>  Query :

    SELECT p.idproducto, p.nombre, p.precio, c.nombre AS cateogoria, m.nombre AS marca
    FROM producto AS p
    LEFT JOIN categoria AS c
    ON p.idcategoria = c.idcategoria
	LEFT JOIN marca AS m
    ON p.idmarca = m.idmarca

### 🖥️ Session 10
- flask
- sqlalchemy
- flask-sqlalchemy