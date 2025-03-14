import mysql.connector


try:
    conn = mysql.connector.connect(
        host="localhost",  
        user="root",      
        password="Benjmax13011.",       
        database="LaPlateforme"
    )

    cursor = conn.cursor()


    query = "SELECT SUM(capacite) AS capacite_totale FROM salle;"
    cursor.execute(query)


    result = cursor.fetchone()


    print(f"La capacité totale des salles est de {result[0]} personnes")

except mysql.connector.Error as err:
    print("Erreur :", err)


