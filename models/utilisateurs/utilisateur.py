   from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
import enum
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
    
    
 

db = SQLAlchemy()

class RoleEnum(enum.Enum):
    ELEVE = "student"
    PROFESSEUR = "teacher"
    ADMIN = "admin"

class Utilisateur(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(200), nullable=False)
    role = db.Column(db.Enum(RoleEnum), nullable=False)

    def set_password(self, password):
        self.mot_de_passe = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.mot_de_passe, password)

