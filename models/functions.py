from config import connection
from models.utilisateurs.utilisateur import User


mydb = connection()

def getuser(email, password):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM utilisateur WHERE email = %s AND password = %s", (email,password))
        result = cursor.fetchone()
        if result :
            # print(result)
            return User(
                result[0],
                result[1],
                result[2],
                result[3],
                result[4],
                result[5],
                result[6]
            )
            
def get_status(email):
        cursor = mydb.cursor()
        cursor.execute("SELECT status FROM utilisateur WHERE email = %s", (email,))
        status = cursor.fetchone()
        print (email)
        return status[0]
    
def update_status(email, status):
        cursor = mydb.cursor()
        cursor.execute("UPDATE utilisateur SET status = %s WHERE email = %s", (status, email))
        mydb.commit()
    
def getProfile(email):
    cursor = mydb.cursor()
    cursor.execute("SELECT profile FROM utilisateur WHERE email = %s", (email,))
    profile = cursor.fetchone()
    return profile[0]

def getAllUsers():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM utilisateur WHERE profile = 'medecin' and profile = 'sécretaire'")
    users = cursor.fetchall()
    return users

def login(email, password):
        # print(email)
        try:
            if get_status(email) != 'online':
                print("iciiiiiiiiii")
                cursor = mydb.cursor()
                query = "SELECT * FROM utilisateur WHERE email = %s AND password = %s"
                values = (email, password)
                cursor.execute(query, values)
                result = cursor.fetchone()
                if result:
                    update_status(email, 'online')
                    id = result[0]
                    name = result[1]
                    surname = result[2]
                    profile = result[4]
                    status = result[5]
                    user = User(id, name, surname, email, password, profile, status)
                    return user
                else:
                      return None
        except Exception as e:
            return None