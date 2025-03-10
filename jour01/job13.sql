mysql> INSERT INTO etudiant (nom, prenom, age, email)
    -> VALUES
    -> ('dupuis','martin',18,'martin.dupuis@laplateforme.io');
Query OK, 1 row affected (0.02 sec)

mysql> SELECT *
    -> FROM etudiant
    -> WHERE nom = 'dupuis'
    -> ;
+----+--------+----------+-----+---------------------------------+
| id | nom    | prenom   | age | email                           |
+----+--------+----------+-----+---------------------------------+
|  5 | Dupuis | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | dupuis | martin   |  18 | martin.dupuis@laplateforme.io   |
+----+--------+----------+-----+---------------------------------+
2 rows in set (0.00 sec)