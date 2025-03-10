mysql> use laplateforme
Database changed
mysql> SELECT id, nom, age
    -> FROM etudiant
    -> WHERE age < 18;
+----+--------+-----+
| id | nom    | age |
+----+--------+-----+
|  4 | Barnes |  16 |
+----+--------+-----+
1 row in set (0.00 sec)

mysql>
