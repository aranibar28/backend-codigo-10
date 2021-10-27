use mydb;

INSERT INTO categoria (nombre) VALUES ("Autos");
INSERT INTO categoria (nombre) VALUES ("Motos");
INSERT INTO categoria (nombre) VALUES ("Aereoplanos");
INSERT INTO categoria (nombre) VALUES ("Barcos");

INSERT INTO marca (nombre) VALUES ("Bugatti");
INSERT INTO marca (nombre) VALUES ("Lamborghini");
INSERT INTO marca (nombre) VALUES ("Audi");

INSERT INTO producto (nombre, fechProduccion, precio, descripcion, idcategoria, idmarca)
VALUES ("Beyron Rojo", "2019-03-12", 100000.0, "Full Equipo", 1, 1);
INSERT INTO producto (nombre, fechProduccion, precio, descripcion, idcategoria, idmarca)
VALUES ("Aventador Negro", "2020-03-12", 140000.0, "Timon a la derecha", 1, 2);
INSERT INTO producto (nombre, fechProduccion, precio, descripcion, idcategoria, idmarca)
VALUES ("R8 Blanco", "2020-05-12", 80000.0, "Full Equipo", 1, 3);

# INSERTAR PRODUCTO SOLO CON MARCA
INSERT INTO producto (nombre, fechProduccion, precio, descripcion, idmarca)
VALUES ("Audi TT", "2020-05-12", 100000.0, "Full Equipo", 1);

# INSERTAR PRODUCTO SOLO CON CATEGORIA
INSERT INTO producto (nombre, fechProduccion, precio, descripcion, idcategoria)
VALUES ("Roll Royce Phantom", "2021-05-12", 100000.0, "Full Equipo", 1);

SELECT p.idproducto, p.nombre, p.precio, c.nombre AS cateogoria, m.nombre AS marca
    FROM producto AS p
    LEFT JOIN categoria AS c
    ON p.idcategoria = c.idcategoria
	LEFT JOIN marca AS m
    ON p.idmarca = m.idmarca

SELECT descripcion, AVG(precio), COUNT(idproducto) FROM producto
    GROUP BY descripcion