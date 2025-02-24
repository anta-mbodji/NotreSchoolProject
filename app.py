from flask import Flask, redirect, session
from config import connection  # Import correct
from auth.auth import auth  # Correct si `auth.py` est dans `auth/`
from models import functions
from models.utilisateurs.utilisateur import User
from routes.student import student
from routes.teacher import teacher
from routes.admin import admin


conn = connection()

app = Flask(__name__)
# Enregistrement des Blueprints
app.register_blueprint(auth, url_prefix="/auth")

app.register_blueprint(student, url_prefix='/student')

app.register_blueprint(teacher, url_prefix='/teacher')

app.register_blueprint(admin, url_prefix='/admin')

app.secret_key = "IamBouddha"

@app.route('/')
def home():
    return redirect('/auth/login_user')


@app.route('/route')
def router():
    if('profile' in session):
        return redirect(f'{session['profile']}/dashboard')
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    if 'email' in session:
        User.logout(functions.getuser(session['email']))
        return redirect('/')
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
