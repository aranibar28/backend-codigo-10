USE mydb;

CREATE VIEW cartelera AS 
SELECT idmovie, title, plot, year, CONCAT((length + 15), " min") AS lengthMin 
FROM movie;

SELECT idmovie, title, plot, year, CONCAT((length + 15), " min") AS lengthMin 
FROM cartelera;

SELECT * FROM cartelera;

##################################################################################

DELIMITER //
CREATE FUNCTION Suma(a INT, b INT)
RETURNS INT
DETERMINISTIC
BEGIN 
	DECLARE sum INT;
    SET sum = a + b;
	RETURN sum;
END; //
DELIMITER ;

ALTER VIEW cartelera2 AS
SELECT idmovie, title, plot, year, CONCAT(Suma(length, 15), " min") AS lengthMin 
FROM cartelera;

SELECT * FROM cartelera2;

##################################################################################

CREATE FUNCTION `isOld` (movieYear INT) 
RETURNS VARCHAR(4)
DETERMINISTIC
BEGIN 
	DECLARE current_year INT;
    SET current_year = YEAR(CURRENT_DATE());
    IF current_year - movieYear >= 2 THEN
		RETURN "OLD";
	ELSE
		RETURN "NEW";
	END IF;
END;

ALTER VIEW cartelera2 AS
SELECT idmovie, title, plot, year, CONCAT(Suma(length, 15), " min") AS lengthMin, isOld(year)  
FROM cartelera 

SELECT * FROM cartelera2;

##################################################################################

CREATE FUNCTION `count_movies` ()
RETURNS INT
DETERMINISTIC
BEGIN
	DECLARE counter INT;
	SELECT COUNT(idmovie) INTO counter FROM movie;
	RETURN counter;
END

select movies.count_movies();

##################################################################################

BEGIN
	DECLARE temp INT;
    DECLARE currentDay INT;
    
    SET currentDay = DAY(Current_date());
    SET temp = MOD((currentDay + Days), 31);
    SET FinalDay = temp;
END

##################################################################################
