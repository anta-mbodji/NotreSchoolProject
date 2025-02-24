from flask import Blueprint, render_template

student = Blueprint('student', __name__)

@student.route('/home')
def home():
    # Ici, vous récupérerez les données spécifiques à l'élève (bulletins, feedback, etc.)
    return render_template('dashboard_student.html')
