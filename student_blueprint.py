from flask import Blueprint, render_template
from flask_login import login_required, current_user

student = Blueprint('student', __name__)

@student.route('/home')
def home():
    # Ici, vous récupérerez les données spécifiques à l'élève (bulletins, feedback, etc.)
    return render_template('dashboard_student.html')

@student.route('/profile')
def profile():
    return render_template('profile_student.html')

@student.route('/settings')
@login_required
def settings():
    # You might want to add some context data
    return render_template('settings_student.html', user=current_user)

@student.route('/feedback')
def feedback():
    return render_template('dashboard_student.html')

