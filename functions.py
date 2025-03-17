from models.utilisateurs.utilisateur import User as user
from models.utilisateurs.admin import admin
from config import connection

mydb = connection()

def getuser(email, password):
        try:
            cursor = mydb.cursor()
            cursor.execute("SELECT * FROM utilisateur WHERE email = %s AND password = %s", (email, password))
            result = cursor.fetchone()
            # print(result)
            if result:
                return user(
                    result[0],
                    result[1],
                    result[2],
                    result[3],
                    result[4],
                    result[5],
                    result[6]
                )
            else:
                return None
        except Exception:
            return None
        
def getuserByEmail(email):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM utilisateur WHERE email = %s", (email,))
    result = cursor.fetchone()
    if result:
        return user(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6]
        )
    
def getAdminByEmail(email):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM utilisateur WHERE email = %s", (email,))
    result = cursor.fetchone()
    print (result)
    if result[8]=='admin':
        # print('iccccccccciiiiiiiiiiiiiiiiiiiiiiiiiiiiii')
        return admin(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[7],
            result[8],
        )


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
    print(profile)
    return profile[0]

def getAllUsers():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM utilisateur WHERE profile != 'admin'")
    users = cursor.fetchall()
    return users

# ----------------------------------------------------------------
# get numbers


def get_total_users():
     cursor = mydb.cursor()
     cursor.execute("SELECT COUNT(*) FROM utilisateur where profile != 'admin'")
     total_users = cursor.fetchone()
     return total_users[0]

def get_total_students():
    cursor = mydb.cursor()
    cursor.execute("SELECT COUNT(*) FROM utilisateur where profile = 'student'")
    total_students = cursor.fetchone()
    return total_students[0]

def getAllStudents():
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM utilisateur where profile = 'student'")
    students = cursor.fetchall()
    return students

def get_total_teachers():
     cursor = mydb.cursor()
     cursor.execute("SELECT COUNT(*) FROM utilisateur WHERE profile = 'teacher'")
     total_teachers = cursor.fetchone()
     return total_teachers[0]

def generate_ID_Student():
    cursor = mydb.cursor()
    cursor.execute("SELECT count(*) FROM utilisateur where profile = 'student'")
    max_id = cursor.fetchone()
    id_user = f"STUD{int(max_id[0]) + 1:06d}"
    return id_user