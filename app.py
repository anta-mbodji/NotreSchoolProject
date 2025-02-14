from flask import Flask
from config import Config  # Import correct
from auth.auth import auth  # Correct si `auth.py` est dans `auth/`

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = "votre_cle_secrete"

    # Enregistrement des Blueprints
    app.register_blueprint(auth, url_prefix="/auth")

    from routes.dashboard_student import dashboard_student as ds_blueprint
    app.register_blueprint(ds_blueprint, url_prefix='/dashboard/student')

    from routes.dashboard_teacher import dashboard_teacher as dt_blueprint
    app.register_blueprint(dt_blueprint, url_prefix='/dashboard/teacher')

    from routes.dashboard_admin import dashboard_admin as da_blueprint
    app.register_blueprint(da_blueprint, url_prefix='/dashboard/admin')

    @app.route('/')  
    def home():
        return "Bienvenue sur Notre School Project !"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
