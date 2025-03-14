import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

def get_connection():
    return mysql.connector.connect(host="localhost", user="root", password="Benjmax13011.", database="store")


def fetch_products():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, name, price, quantity FROM product")
    products = cursor.fetchall()
    connection.close()
    return products

def add_product():
    name, price, quantity = entry_name.get(), entry_price.get(), entry_quantity.get()
    if not (name and price and quantity):
        messagebox.showerror("Erreur", "Veuillez remplir tous les champs")
        return
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO product (name, price, quantity) VALUES (%s, %s, %s)", (name, price, quantity))
    connection.commit()
    connection.close()
    refresh_table()
    messagebox.showinfo("Succès", "Produit ajouté avec succès")

def delete_product():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Erreur", "Veuillez sélectionner un produit")
        return
    product_id = tree.item(selected_item)['values'][0]
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
    connection.commit()
    connection.close()
    refresh_table()
    messagebox.showinfo("Succès", "Produit supprimé")

def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    for product in fetch_products():
        tree.insert("", "end", values=product)

root = tk.Tk()
root.title("Gestion de Stock")

tk.Label(root, text="Nom:").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Prix:").pack()
entry_price = tk.Entry(root)
entry_price.pack()

tk.Label(root, text="Quantité:").pack()
entry_quantity = tk.Entry(root)
entry_quantity.pack()

tk.Button(root, text="Ajouter Produit", command=add_product).pack()
tk.Button(root, text="Supprimer Produit", command=delete_product).pack()

columns = ("ID", "Nom", "Prix", "Quantité")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)
tree.pack()

refresh_table()
root.mainloop()
