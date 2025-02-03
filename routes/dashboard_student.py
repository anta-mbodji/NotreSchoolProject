from flask import Blueprint, render_template

dashboard_student = Blueprint('dashboard_student', __name__)

@dashboard_student.route('/home')
def home():
    # Ici, vous récupérerez les données spécifiques à l'élève (bulletins, feedback, etc.)
    return render_template('dashboard_student.html')
