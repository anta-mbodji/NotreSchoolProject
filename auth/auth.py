from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
import models.functions as func
from models.utilisateurs.utilisateur import User as user


from config import connection # Import correct de la configuration

from flask import Blueprint

auth = Blueprint('auth', __name__)


# Fonction pour obtenir une connexion PostgreSQL

# @auth.route('/register', methods=['GET', 'POST'])
# def register():
#     roles = ['student', 'teacher', 'admin']
#     if request.method == 'POST':
#         email = request.form.get('email')
#         password = request.form.get('password')
#         first_name = request.form.get('first_name')  # Correction ici
#         last_name = request.form.get('last_name')
#         role = request.form.get('role')
#         school_id = request.form.get('school_id')
#         class_id = request.form.get('class_id') if role == 'student' else None

#         password_hash = generate_password_hash(password)

#         conn = connection()
#         cur = conn.cursor()
#         try:
#             cur.execute("""
#                 INSERT INTO users (email, password_hash, first_name, last_name, role, school_id, class_id)
#                 VALUES (%s, %s, %s, %s, %s, %s, %s)
#                 RETURNING id;
#             """, (email, password_hash, first_name, last_name, role, school_id, class_id))
#             conn.commit()
#             flash("Inscription réussie !", "success")
#         except psycopg2.Error as e:
#             flash(f"Erreur lors de l'inscription : {e.pgerror}", "danger")
#         finally:
#             cur.close()
#             conn.close()

#         return redirect(url_for('auth.login'))
    
#     return render_template('register.html', roles=roles)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    error_message = None
    # if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('mdpass')
    result = func.login(email, password)
    if result is not None:
        session['email'] = result.email
        session['profile'] = func.getProfile(email)
        return redirect('/route')
    else:
        print(f"l'utilisateur n'existe pas")
        error_message = f"user does not exist"
        return render_template('login.html', error_message=error_message)
        
@auth.route('/register_user', methods=['GET', 'POST'])
def register_user():
    # print("Route /register appelée")  # <-- Debugging
    return render_template('register.html')

@auth.route('/login_user', methods=['GET', 'POST'])
def login_user():
    # print("Route /login appelée")  # <-- Debugging
    return render_template('login.html')

@auth.route('/forgot_password', methods=['POST'])
def forgot_password():
    email = request.form.get('email')

    # Dummy check - in a real app, check if email exists in DB
    if email == "user@example.com":
        return "Password reset link sent to your email!"
    else:
        return render_template('login.html', error_message="Email not found! Try again.")

    
@auth.errorhandler(404)
def page_not_found(e):
    return redirect('/')