# CREAR VISTA CARTELERA 
CREATE VIEW cartelera AS 
SELECT idmovie, title, plot, year, CONCAT((length + 15), " min") AS lengthMin 
FROM movie;

# MODIFICAR VISTA CARTELERA 
ALTER VIEW cartelera AS 
SELECT idmovie, title, year, CONCAT(length + 15, " min") AS lengthMin 
FROM movie;