import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",      
        password="Benjmax13011.",      
        database="LaPlateforme"
    )

    cursor = conn.cursor()


    query = "SELECT * FROM etudiant;"
    cursor.execute(query)


    students = cursor.fetchallS()
    for student in students:
        print(student)

except mysql.connector.Error as err:
    print("Erreur :")


