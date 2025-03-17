from models.utilisateurs.utilisateur import User


class student(User):
    def __init__(self, id_user, name, surname, email, password, profile, status, grade):
        super().__init__(id_user, name, surname, email, password, profile, status)
        self._grade = grade

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
        return self._grade
    
