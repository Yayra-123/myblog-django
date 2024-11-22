import sqlite3


# Nom de la base de données
database = 'db.sqlite3'

try:
    # Établir une connexion à la base de données
    conn = sqlite3.connect(database)

    # Créer un curseur pour exécuter les requêtes SQL
    cur = conn.cursor()

    # Créer la table si elle n'existe pas déjà
    # cur.execute(
    #     "CREATE TABLE IF NOT EXISTS Post(title TEXT, content TEXT)"
    # )

    # Insérer le premier article de blog
    cur.execute(
        "INSERT INTO posts_post(title, content) VALUES (?, ?)",
        ('la reine pokou', 'le prince de la tribu baoulé ,desirais vivement mariée la princesse mais malheureusement pour lui la reine s\'interressait au fermier')
    )

    # Insérer le second article de blog
    cur.execute(
        "INSERT INTO posts_post(title, content) VALUES (?, ?)",
        ('la meilleur journée', 'une journée sans soucis ou tu ne fais que coder')
    )

    # Valider les modifications dans la base de données
    conn.commit()

    # Afficher un message de succès
    print("Les articles de blog ont été insérés avec succès.")

except Exception as e:
    # Gérer l'erreur
    print(f"Une erreur s'est produite : {e}")

finally:
    # Fermer la connexion à la base de données
    if conn:
        conn.close()
