import psycopg2
class Config:
    SECRET_KEY = "your_secret_key"

    DATABASE_URL = "postgresql://postgres:postGres@localhost:5433/schoolproject"

def get_db_connection():
    conn = psycopg2.connect(DATABASE_URL)
    return conn
