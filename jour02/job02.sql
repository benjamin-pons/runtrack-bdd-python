mysql> create table etage
    -> ( id INT AUTO_INCREMENT PRIMARY KEY,
    -> nom VARCHAR (255),
    -> numero INT,
    -> superficie INT
    -> );
Query OK, 0 rows affected (0.16 sec)

 CREATE TABLE salle (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     id_etage INT,
    ->     capacite INT,
    ->     FOREIGN KEY (id_etage) REFERENCES etage(id) ON DELETE CASCADE
    -> );
Query OK, 0 rows affected (0.21 sec)