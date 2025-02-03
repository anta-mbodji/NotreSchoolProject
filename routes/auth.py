from flask import Blueprint, render_template, request, redirect, url_for, Flask
from werkzeug.security import generate_password_hash, check_password_hash

import psycopg2

auth = Blueprint('auth', __name__)

def get_df_connection():
    from config import config
    conn = psycopg2.connect(
        database = config.database,
        user = config.user,
        password = config.password,
        host = config.host ,
        port = config.port
    )
    return conn

@auth.route('/register', methods=['GET', 'POST'])
def register():
    role = ['student','teacher','admin']
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        first_namename = request.form.get('first_name')
        last_name = request.form.get('last_name')
        role = request.form.get('role')
        school_id = request.form.get('school_id')
        class_id = request.form.get('class_id') if role == 'student' else None


        password_hash = generate_password_hash(password)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO users (email, password_hash, first_name, last_name, role, school_id, class_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            RETURNING id;
        """, (email, password_hash, first_name, last_name, role, school_id, class_id))
        conn.commit()
        cur.close()
        conn.close()
        flash("Inscription réussie !", "success")
        return redirect(url_for('auth.login'))
    return render_template('register.html')

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

        if user and check_password_hash(user[1], password):
            # Pour l'instant, vous pouvez simplement rediriger en fonction du rôle
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
