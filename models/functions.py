from config import connection


mydb = connection()


def getuser(email):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM utilisateur WHERE email = %s", (email,))
        result = cursor.fetchone()
        # if result[5] == 'admin':
        #     # print(result)
        #     return Admin(
        #         result[0],
        #         result[1],
        #         result[2],
        #         result[3],
        #         result[4],
        #         result[5],
        #         result[6]
        #     )
        # else:
        #     return user(
        #         result[0],
        #         result[1],
        #         result[2],
        #         result[3],
        #         result[4],
        #         result[5],
        #         result[6]
        #     )
            
def get_status(email):
        cursor = mydb.cursor()
        cursor.execute("SELECT status FROM utilisateur WHERE email = %s", (email,))
        status = cursor.fetchone()
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