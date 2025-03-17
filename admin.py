#import modules
from models.utilisateurs.utilisateur import User
from models.utilisateurs.teacher import teacher
from models.utilisateurs.student import student
from config import connection as conn

mydb = conn()
#define class admin
class admin(User):
    def __init__(self, id_user, name, surname, email, password, status, profile):
        super().__init__(id_user, name, surname, email, password, status, profile)
        
    def add_user(self, id_user, name, surname, email, password, profile, status, grade):
        print(self.name)
        
        if self.profile == 'admin':
            # print(f'Student {name} {surname} created successfully.')
            # Insert user in the database
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO utilisateur (id, name, surname, email, password, profile, status, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (id_user, name, surname, email, password, profile, status, grade)
                mycursor.execute(sql, val)
                mydb.commit()
                return (True,f"user inserted successfully")
            except Exception as e:
                print(f"Error: {e}")
                return (False,f"{e}")
        else:
            print('Only admin can add users.')
            return (False,f"Only admin can add users")