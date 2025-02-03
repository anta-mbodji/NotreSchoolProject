from flask import Flask, render_template
from config import config 

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)


    from routes.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from routes.dashboard_student import dashboard_student as ds_blueprint
    app.register_blueprint(ds_blueprint, url_prefixe='/bashboard/student')

    from routes.dashboard_teacher import dashboard_teacher as dt_blueprint
    app.register_blueprint(dt_blueprint, url_prefixe='/bashboard/teacher')

    from routes.dashboard_admin import dashboard_admin as da_blueprint
    app.register_blueprint(da_blueprint, url_prefixe='/bashboard/admin')

    @app.route('/')  # Route pour la page d'accueil
    def home():
        return "Bienvenue sur Notre School Project !"

    

    return app


if __name__ == '__main__' :
    app = create_app()
    app.run(debug=True)  # Run the app in debug mode.