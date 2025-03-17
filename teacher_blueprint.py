from flask import Blueprint, render_template
from models.utilisateurs.teacher import teacher

teacher = Blueprint('teacher', __name__)

@teacher.route('/dashboard_teacher')
def dashboard():
    return "Tableau de bord de l'enseignant"

@teacher.route('/notes')
def notes():
    return render_template('teacher/notes.html')


