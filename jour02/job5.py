import mysql.connector


try:
    conn = mysql.connector.connect(
        host="localhost",  
        user="root",      
        password="Benjmax13011.",       
        database="LaPlateforme"
    )

    cursor = conn.cursor()


    query = "SELECT SUM(superficie) AS superficie_totale FROM etage;"
    cursor.execute(query)


    result = cursor.fetchone()


    print(f"La superficie de La Plateforme est de {result[0]} m2")

except mysql.connector.Error as err:
    print("Erreur :", err)


