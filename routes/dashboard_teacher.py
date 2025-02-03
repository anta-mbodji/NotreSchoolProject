from flask import Blueprint, render_template

dashboard_teacher = Blueprint('dashboard_teacher', __name__)

@dashboard_teacher.route('/dashboard_teacher')
def dashboard():
    return "Tableau de bord de l'enseignant"
