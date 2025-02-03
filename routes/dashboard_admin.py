from flask import Blueprint, render_template

dashboard_admin = Blueprint('dashboard_admin', __name__)

@dashboard_admin.route('/dashboard_admin')
def dashboard():
    return "Tableau de bord de l'administrateur"
