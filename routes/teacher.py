from flask import Blueprint, render_template

teacher = Blueprint('teacher', __name__)

@teacher.route('/dashboard_teacher')
def dashboard():
    return "Tableau de bord de l'enseignant"
