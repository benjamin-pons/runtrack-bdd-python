import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox

class StockManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Stock")
        self.root.geometry("800x500")

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="store"
        )
        self.cursor = self.conn.cursor()

        self.create_tables()
        self.create_ui()
        self.load_products()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS category (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL
        )""")

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS product (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price INT NOT NULL,
            quantity INT NOT NULL,
            id_category INT,
            FOREIGN KEY (id_category) REFERENCES category(id) ON DELETE SET NULL
        )""")
        self.conn.commit()

    def create_ui(self):
        self.tree = ttk.Treeview(self.root, columns=("ID", "Nom", "Description", "Prix", "Stock", "Catégorie"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Prix", text="Prix")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Catégorie", text="Catégorie")
        self.tree.pack(fill=tk.BOTH, expand=True)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack()
        
        add_btn = tk.Button(btn_frame, text="Ajouter Produit", command=self.add_product)
        add_btn.pack(side=tk.LEFT, padx=10)
        
        update_btn = tk.Button(btn_frame, text="Modifier Produit", command=self.update_product)
        update_btn.pack(side=tk.LEFT, padx=10)
        
        delete_btn = tk.Button(btn_frame, text="Supprimer Produit", command=self.delete_product)
        delete_btn.pack(side=tk.LEFT, padx=10)

    def load_products(self):
        self.tree.delete(*self.tree.get_children())
        self.cursor.execute("SELECT product.id, product.name, product.description, product.price, product.quantity, category.name FROM product LEFT JOIN category ON product.id_category = category.id")
        for row in self.cursor.fetchall():
            self.tree.insert("", "end", values=row)

    def add_product(self):
        # Exemple simple : ici, il faudrait créer une autre fenêtre pour entrer les données
        self.cursor.execute("INSERT INTO product (name, description, price, quantity, id_category) VALUES ('Produit test', 'Description test', 100, 10, 1)")
        self.conn.commit()
        self.load_products()

    def update_product(self):
        # À implémenter : modifier un produit sélectionné
        messagebox.showinfo("Modifier", "Modification à implémenter")

    def delete_product(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Suppression", "Veuillez sélectionner un produit à supprimer")
            return
        product_id = self.tree.item(selected_item, "values")[0]
        self.cursor.execute("DELETE FROM product WHERE id = %s", (product_id,))
        self.conn.commit()
        self.load_products()
        messagebox.showinfo("Suppression", "Produit supprimé avec succès")

if __name__ == "__main__":
    root = tk.Tk()
    app = StockManager(root)
    root.mainloop()
