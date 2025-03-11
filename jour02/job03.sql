mysql> INSERT INTO etage (nom, numero, superficie)
    -> VALUES ('RDC', 0, 500);
Query OK, 1 row affected (0.06 sec)

mysql>
mysql> INSERT INTO etage (nom, numero, superficie)
    -> VALUES ('R+1', 1, 500);
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite)
    -> VALUES ( 'lounge', 1, 100);
Query OK, 1 row affected (0.06 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite)
    -> VALUES ( 'studio son', 1, 5);
Query OK, 1 row affected (0.06 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite)
    -> VALUES ( 'Broadcasting', 2, 50);
Query OK, 1 row affected (0.06 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite)
    -> VALUES ( 'Bocal Peda', 2, 4);
Query OK, 1 row affected (0.02 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite)
    -> VALUES ( 'Coworking', 2, 80);
Query OK, 1 row affected (0.06 sec)

mysql> INSERT INTO salle (nom, id_etage, capacite)
    -> VALUES ( 'Studio video', 2, 5);
Query OK, 1 row affected (0.06 sec)