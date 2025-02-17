from werkzeug.security import generate_password_hash, check_password_hash
import enum
from flask import Flask, session, redirect, render_template
from config import connection as conn
import models.functions as func

mydb = conn
class User:
    def __init__(self, id_user, surname, name, email, password):
        self._id_user = id_user
        self._surname = surname
        self._name = name
        self._email = email
        self._password = password
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        return self._name
    
    @property
    def surname(self):
        return self._surname
        
    @surname.setter
    def surname(self, surname):
        self._surname = surname
        return self._surname
    
    @property
    def email(self):
        return self._email
        
    @email.setter
    def email(self, email):
        self._email = email
        return self._email
        
    @property
    def password(self):
        return self._password
        
    @password.setter
    def password(self, password):
        self._password = generate_password_hash(password)
        return self._password
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def login(self):
        # print(self._email)
        if func.get_status(self.email) != 'online':
            cursor = mydb.cursor()
            query = "SELECT * FROM utilisateur WHERE email = %s AND password = %s"
            values = (self.email, self._password)
            cursor.execute(query, values)
            result = cursor.fetchone()
            if result:
                func.update_status(self.email, 'online')
                session['id'] = result[0]
                session['name'] = result[1]
                session['surname'] = result[2]
                session['email'] = result[3]
                session['profile'] = result[4]
                session['status'] = result[5]
                return (True)
            else:
                return (False)
        else:
            return self.email + ' is already connected'
        
    def logout(self):
        func.update_status(self.email, 'offline')
        session.pop('email', None)
        session.pop('profile', None)
        return redirect('/')
    
    def isconnected(username):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM utilisateur WHERE email = %s AND status = %s", (username, 'online'))
        account = cursor.fetchone()
        if account:
            return account
        else:
            return False
        
# class RoleEnum(enum.Enum):
#     ELEVE = "student"
#     PROFESSEUR = "teacher"
#     ADMIN = "admin"
