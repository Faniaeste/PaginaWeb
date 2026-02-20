Seleccionar todos los registros de una tabla
SELECT * FORM Clientes;
Seleccionar algunos campos de una tabla de base de datos
SELECT Nombre, Edad FROM Clientes;
Para insertar nuevos registros en la tabla
INSERT INTO Clientes (Nombre,Edad,Email) VALUES ("Antonio",37,"Antoniocbr@gmail.com");
Para actualizar registros de la tabla de la base de datos, siempre usar WHERE
UPDATE Clientes SET nombre = "Devora" WHERE id = 1;
Seleccionar con WHERE
SELECT * FROM Clientes WHERE Edad >50;
Comando para borrar registros, importante utilizar siempre el WHERE,
sino borrariamos todos los campos de la tabla
DELETE FROM Clientes WHERE id 2;
Consulta select con orden aplicado
SELECT * FROM Clientes ORDER BY Edad ASC;