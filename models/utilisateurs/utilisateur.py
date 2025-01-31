
class User:
    def __init__(self, id_user, surname, name, email, password):
        self.id_user = id_user
        self.surname = surname
        self.name = name
        self.email = email
        self.password = password
    
    @property
    def full_name(self):
        return f"{self.surname} {self.name}"
    
    @name.setter
    def name(self, name):
        self.name = name
        return self.name
    
    