mysql> USE laplateforme
Database changed
mysql> SELECT id, nom, age
    -> FROM etudiant
    -> ORDER BY age ASC;
+----+-----------+-----+
| id | nom       | age |
+----+-----------+-----+
|  4 | Barnes    |  16 |
|  3 | Doe       |  18 |
|  5 | Dupuis    |  20 |
|  1 | Spaghetti |  23 |
|  2 | Steak     |  45 |
+----+-----------+-----+
5 rows in set (0.00 sec)

mysql>
