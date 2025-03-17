from flask import Flask,redirect, session
from config import connection as conn
from models import functions as func

mydb = conn()

class User:
    def __init__(self, id_user, name, surname, email, password, status, profile):
        self._id_user = id_user
        self._name = name
        self._surname = surname
        self._email = email
        self._password = password
        self._profile = profile
        self._status = status
    
    @property
    def id_user(self):
        return self._id_user
    
    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user
        return self._id_user
    
    @property
    def name(self):
        return self._name
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def email(self):
        return self._email
    
    @property
    def profile(self):
        return self._profile
    
    @profile.setter
    def profile(self, profile):
        self._profile = profile
        return self._profile
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
        return self._password
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
        return self._status
    
    @name.setter
    def name(self, name):
        self._name = name
        return self._name
    
    @surname.setter
    def surname(self, surname):
        self._surname = surname
        return self._surname
    
    @email.setter
    def email(self, email):
        self._email = email
        return self._email
    
    def login(self):
        # print(self._email)
        try:
            if(self.email is None):
                return 'email not found'
            else:
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
        except Exception as e:
            return str(e)
        
    def logout(self):
        try:
            func.update_status(self.email, 'offline')
            session.pop('email', None)
            session.pop('profile', None)
            return redirect('/')
        except Exception as e:
            return str(e)
    
    def isconnected(username):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM utilisateur WHERE email = %s AND status = %s", (username, 'online'))
        account = cursor.fetchone()
        if account:
            return account
        else:
            return False
        