from models.utilisateurs.utilisateur import User
from models.utilisateurs.student import student
from config import connection

mydb = connection()

class teacher(User):
    def __init__(self, id_user, name, surname, email, password, profile, status, speciality):
        super().__init__(id_user, name, surname, email, password, profile, status)
        self._speciality = speciality

    @property
    def speciality(self):
        return self._speciality
    
    @speciality.setter
    def speciality(self, speciality):
        self._speciality = speciality
        return self._speciality
    
    
    def create_note(self, id_student, note):
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO notes (id_student, note, id_teacher) VALUES (%s, %s, %s)", (id_student, note, self.id_user))
        mydb.commit()
        cursor.close()
    
    def get_notes(self, id_student):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM notes WHERE id_student = %s", (id_student,))
        notes = cursor.fetchall()
        cursor.close()
        return notes

    def get_all_notes(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM notes")
        notes = cursor.fetchall()
        cursor.close()
        return notes

    def get_note_by_id(self, id_student):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM notes WHERE id_student = %s", (id_student,))
        note = cursor.fetchone()
        cursor.close()
        return note
    
    def get_all_students(self):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM students WHERE id_teacher = %s", (self.id_user,))
        students = cursor.fetchall()
        cursor.close()
        return students

    def get_student_by_id(self, id_student):
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM students WHERE id_student = %s", (id_student,))
        student = cursor.fetchone()
        cursor.close()
        return student

    