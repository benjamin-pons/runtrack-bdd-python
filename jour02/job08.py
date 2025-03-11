import mysql.connector

# Connexion à la base de données
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Benjmax13011.",
    database="zoo"
)
cursor = conn.cursor()

# Affichage du menu
def afficher_menu():
    print("\nMenu :")
    print("1. Ajouter un animal")
    print("2. Supprimer un animal")
    print("3. Afficher tous les animaux")
    print("4. Afficher les cages")
    print("5. Calculer la superficie totale des cages")
    print("6. Quitter")

# Ajouter un animal
def ajouter_animal():
    nom = input("Nom de l'animal : ")
    race = input("Race de l'animal : ")
    cage_id = input("ID de la cage (laisser vide si aucune cage) : ")
    date_naissance = input("Date de naissance (YYYY-MM-DD) : ")
    pays_origine = input("Pays d'origine : ")

    cage_id = None if cage_id == "" else int(cage_id)

    query = "INSERT INTO animal (nom, race, cage_id, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (nom, race, cage_id, date_naissance, pays_origine))
    conn.commit()
    print("Animal ajouté.")

# Supprimer un animal
def supprimer_animal():
    animal_id = input("ID de l'animal à supprimer : ")
    query = "DELETE FROM animal WHERE animal_id = %s"
    cursor.execute(query, (animal_id,))
    conn.commit()
    print("Animal supprimé.")

# Afficher tous les animaux
def afficher_animaux():
    query = "SELECT * FROM animal"
    cursor.execute(query)
    animaux = cursor.fetchall()
    print("\nListe des animaux :")
    for animal in animaux:
        print(animal)

# Afficher les cages
def afficher_cages():
    query = "SELECT * FROM cage"
    cursor.execute(query)
    cages = cursor.fetchall()
    print("\nListe des cages :")
    for cage in cages:
        print(cage)

# Calculer la superficie totale des cages
def superficie_totale_cages():
    query = "SELECT SUM(superficie) FROM cage"
    cursor.execute(query)
    total = cursor.fetchone()[0]
    print(f"\nSuperficie totale des cages : {total} m²")

# Programme principal
def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            ajouter_animal()
        elif choix == "2":
            supprimer_animal()
        elif choix == "3":
            afficher_animaux()
        elif choix == "4":
            afficher_cages()
        elif choix == "5":
            superficie_totale_cages()
        elif choix == "6":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
