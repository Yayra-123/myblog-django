import sqlite3

# Nom de la base de données
database = 'db.sqlite3'


    # Établir une connexion à la base de données
conn = sqlite3.connect(database)

    # Créer un curseur pour exécuter les requêtes SQL
cur = conn.cursor()

    # Sélectionner tous les articles de blog
cur.execute("SELECT * FROM posts_post")

    # Récupérer les résultats
rows =list(cur)
print(rows)
    

    

