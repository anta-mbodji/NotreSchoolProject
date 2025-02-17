import psycopg2


def connection():
    # Configuration de la connexion à la base de données
    conn = psycopg2.connect(
        dbname='ecole_db',         # Remplacez par le nom de votre base de données
        user='bouddha',         # Remplacez par votre utilisateur PostgreSQL
        password='logyouin',  # Remplacez par votre mot de passe
        host='localhost',
        port='5432'
    )
    return conn
