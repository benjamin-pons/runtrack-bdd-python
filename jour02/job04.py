import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",      
        password="Benjmax13011.",      
        database="LaPlateforme"
    )

    cursor = conn.cursor()


    query = "SELECT nom , capacite FROM salle;"
    cursor.execute(query)


    salles = cursor.fetchall()
    for salle in salles:
        print(f"Nom de la salle : {salle[0]}, Capacité : {salle[1]}")


except mysql.connector.Error as err:
    print("Erreur :", err)