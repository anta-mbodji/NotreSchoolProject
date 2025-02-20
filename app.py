from flask import Flask, redirect, session
from config import connection  # Import correct
from auth.auth import auth  # Correct si `auth.py` est dans `auth/`
from routes.dashboard_student import dashboard_student as ds_blueprint
from routes.dashboard_teacher import dashboard_teacher as dt_blueprint
from routes.dashboard_admin import dashboard_admin as da_blueprint


conn = connection()

app = Flask(__name__)
# Enregistrement des Blueprints
app.register_blueprint(auth, url_prefix="/auth")

app.register_blueprint(ds_blueprint, url_prefix='/dashboard/student')

app.register_blueprint(dt_blueprint, url_prefix='/dashboard/teacher')

app.register_blueprint(da_blueprint, url_prefix='/dashboard/admin')

app.secret_key = "IamBouddha"

@app.route('/')
def home():
    return redirect('/auth/login_user')


@app.route('/route')
def router():
    if('profile' in session):
        return redirect(f'/{session['profile']}/dashboard')
    else:
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
