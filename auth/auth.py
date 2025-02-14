from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2
from config import Config  # Import correct de la configuration

from flask import Blueprint

auth = Blueprint('auth', __name__)


# Fonction pour obtenir une connexion PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        database=Config.database,
        user=Config.user,
        password=Config.password,
        host=Config.host,
        port=Config.port
    )
    return conn

@auth.route('/register', methods=['GET', 'POST'])
def register():
    roles = ['student', 'teacher', 'admin']
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_name = request.form.get('first_name')  # Correction ici
        last_name = request.form.get('last_name')
        role = request.form.get('role')
        school_id = request.form.get('school_id')
        class_id = request.form.get('class_id') if role == 'student' else None

        password_hash = generate_password_hash(password)

        conn = get_db_connection()
        cur = conn.cursor()
        try:
            cur.execute("""
                INSERT INTO users (email, password_hash, first_name, last_name, role, school_id, class_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                RETURNING id;
            """, (email, password_hash, first_name, last_name, role, school_id, class_id))
            conn.commit()
            flash("Inscription réussie !", "success")
        except psycopg2.Error as e:
            flash(f"Erreur lors de l'inscription : {e.pgerror}", "danger")
        finally:
            cur.close()
            conn.close()

        return redirect(url_for('auth.login'))
    
    return render_template('register.html', roles=roles)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, password_hash, role FROM users WHERE email = %s", (email,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and check_password_hash(user[1], password):  # Vérification correcte du mot de passe
            user_id, _, role = user
            flash("Connexion réussie", "success")
            if role == 'student':
                return redirect(url_for('dashboard_student.home'))
            elif role == 'teacher':
                return redirect(url_for('dashboard_teacher.home'))
            elif role == 'admin':
                return redirect(url_for('dashboard_admin.home'))
        else:
            flash("Identifiants incorrects", "danger")
    
    return render_template('login.html')
@auth.route('/register_user', methods=['GET', 'POST'])
def register_user():
    print("Route /register appelée")  # <-- Debugging
    return render_template('register.html')

@auth.route('/login_user', methods=['GET', 'POST'])
def login_user():
    print("Route /login appelée")  # <-- Debugging
    return render_template('login.html')
