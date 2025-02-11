from flask import Flask
from config import Config  # Correction de l'import

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Importation et enregistrement des Blueprints
    from routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from routes.dashboard_student import dashboard_student as ds_blueprint
    app.register_blueprint(ds_blueprint, url_prefix='/dashboard/student')  # Correction de `url_prefix`

    from routes.dashboard_teacher import dashboard_teacher as dt_blueprint
    app.register_blueprint(dt_blueprint, url_prefix='/dashboard/teacher')  # Correction de `url_prefix`

    from routes.dashboard_admin import dashboard_admin as da_blueprint
    app.register_blueprint(da_blueprint, url_prefix='/dashboard/admin')  # Correction de `url_prefix`

    @app.route('/')  # Route pour la page d'accueil
    def home():
        return "Bienvenue sur Notre School Project !"

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)  # Lancement de l'application en mode debug
