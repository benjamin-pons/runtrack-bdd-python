mysql> SELECT nom, prenom
    -> FROM etudiant
    -> WHERE prenom LIKE 'B%';
+-----------+--------+
| nom       | prenom |
+-----------+--------+
| Spaghetti | Betty  |
| Barnes    | Binkie |
+-----------+--------+
2 rows in set (0.00 sec)
