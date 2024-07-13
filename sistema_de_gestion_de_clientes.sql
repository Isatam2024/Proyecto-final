DELIMITER //
CREATE PROCEDURE clientes()
BEGIN
    SELECT * FROM clientes;  -- Replace clientes_table with your actual table name
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE AgregarCliente(IN p_ID_cliente INT(11), IN p_Nombre VARCHAR(45), IN p_Email VARCHAR(45), IN p_Telefono VARCHAR(45))
BEGIN
    INSERT INTO clientes (ID_cliente, Nombre, Email, Telefono)  -- Replace clientes_table with your actual table name
    VALUES (p_ID_cliente, p_Nombre, p_Email, p_Telefono);
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ConsultarClientes()
BEGIN
    SELECT * FROM clientes;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE DetalleClientes(IN ID_Cliente INT(11))
BEGIN
    SELECT * FROM clientes WHERE ID_Cliente = ID_Cliente;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarCliente(
    IN ID_cliente INT(11),
    IN Nombre VARCHAR(45),
    IN Email VARCHAR(45),
    IN Telefono VARCHAR(45)
)
BEGIN
    UPDATE clientes
    SET Nombre = Nombre,
        Email = Email,
        Telefono = Telefono
    WHERE ID_cliente = ID_cliente;
END//
DELIMITER ;

DROP PROCEDURE IF EXISTS ActualizarCliente

DELIMITER //
CREATE PROCEDURE ActualizarCliente(
    IN p_id_cliente INT,
    IN p_nombre VARCHAR(45),
    IN p_email VARCHAR(45),
    IN p_telefono VARCHAR(45)
)
BEGIN
    UPDATE clientes
    SET nombre = p_nombre, email = p_email, telefono = p_telefono
    WHERE ID_cliente = p_id_cliente;
END//
DELIMITER ;

DELIMITER //
CREATE PROCEDURE EliminarCliente(
    IN p_id_cliente INT
)
BEGIN
    DELETE FROM clientes
    WHERE ID_cliente = p_id_cliente;
END//
DELIMITER ;
