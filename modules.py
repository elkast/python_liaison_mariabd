import mysql.connector

def envoyer_donnees(nom, email, config):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO utilisateurs (nom, email) VALUES (%s, %s)", (nom, email))
    conn.commit()
    cursor.close()
    conn.close()

def lire_donnees(config):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilisateurs")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
