Enter password: *************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 13
Server version: 8.0.41 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE DATABASE <LaPlateforme>
    -> ^C
mysql> CREATE DATABASE <LAPLATEFORME>
    ->
    ->
    -> ^C
mysql> create database LaPlateforme
    -> ^C
mysql> create database LaPlateforme;
Query OK, 1 row affected (0.07 sec)

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| laplateforme       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.06 sec)

mysql> use LaPlateforme
Database changed
mysql> create table etudiant
    -> create table etudiant;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'create table etudiant' at line 2
mysql> create table etudiant(
    ->
    -> ^C
mysql> create table etudiant(
    -> id (int)
    -> nom (varchar 255)
    -> prenom (varchar 25)
    -> age (int)
    -> email (varchar 255)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(int)
nom (varchar 255)
prenom (varchar 25)
age (int)
email (varchar 255)
)' at line 2
mysql> CREATE TABLE etudiant (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255) NOT NULL,
    ->     prenom VARCHAR(25) NOT NULL,
    ->     age INT NOT NULL,
    ->     email VARCHAR(255) NOT NULL
    -> );
Query OK, 0 rows affected (0.11 sec)

mysql> show table
    -> show table;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'show table' at line 2
mysql> show table;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '' at line 1
mysql> show tables;
+------------------------+
| Tables_in_laplateforme |
+------------------------+
| etudiant               |
+------------------------+
1 row in set (0.06 sec)

mysql> show databases
    -> ;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| laplateforme       |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)


mysql> use laplateforme
Database changed
mysql> SHOW COLUMNS FROM etudiant;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nom    | varchar(255) | NO   |     | NULL    |                |
| prenom | varchar(25)  | NO   |     | NULL    |                |
| age    | int          | NO   |     | NULL    |                |
| email  | varchar(255) | NO   |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
5 rows in set (0.01 sec)

mysql> SHOW COLUMNS FROM etudiant;
ERROR 1046 (3D000): No database selected
mysql> SHOW COLUMNS FROM etudiant;
ERROR 1046 (3D000): No database selected
mysql> use laplateforme
Database changed
mysql> SHOW COLUMNS FROM etudiant;
+--------+--------------+------+-----+---------+----------------+
| Field  | Type         | Null | Key | Default | Extra          |
+--------+--------------+------+-----+---------+----------------+
| id     | int          | NO   | PRI | NULL    | auto_increment |
| nom    | varchar(255) | NO   |     | NULL    |                |
| prenom | varchar(25)  | NO   |     | NULL    |                |
| age    | int          | NO   |     | NULL    |                |
| email  | varchar(255) | NO   |     | NULL    |                |
+--------+--------------+------+-----+---------+----------------+
5 rows in set (0.00 sec)

mysql> INSERT INTO etudiant (nom, prenom, age, email)
    -> VALUES
    -> ('Spaghetti', 'Betty', 23, 'betty.spaghetti@laplateforme.io'),
    -> ('Steak', 'Chuck', 45, 'chuck.steak@laplateforme.io'),
    -> ('Doe', 'John', 18, 'john.doe@laplateforme.io'),
    -> ('Barnes', 'Binkie', 16, 'binkie.barnes@laplateforme.io'),
    -> ('Dupuis', 'Gertrude', 20, 'gertrude.dupuis@laplateforme.io');
Query OK, 5 rows affected (0.04 sec)
Records: 5  Duplicates: 0  Warnings: 0

mysql> show etudiant;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'etudiant' at line 1
mysql> select * from etudiant;
ERROR 1046 (3D000): No database selected
mysql> use laplateforme
Database changed
mysql> select * from etudiant;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | Spaghetti | Betty    |  23 | betty.spaghetti@laplateforme.io |
|  2 | Steak     | Chuck    |  45 | chuck.steak@laplateforme.io     |
|  3 | Doe       | John     |  18 | john.doe@laplateforme.io        |
|  4 | Barnes    | Binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | Dupuis    | Gertrude |  20 | gertrude.dupuis@laplateforme.io |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0.00 sec)

mysql>

