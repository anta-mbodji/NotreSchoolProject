from flask import Blueprint, flash, render_template, redirect, session, request
from models.utilisateurs.student import student
from config import connection
import models.functions as func

admin = Blueprint('admin', __name__)

@admin.route('/dashboard')
def dashboard():
    if 'email' in session:
        # if session['profile'] == 'admin':
        #     # print(session['email'])
        #     # print(session['name'])
        #     # print(session['profile'])

        total_users = func.get_total_users()
        total_students = func.get_total_students()
        total_teachers = func.get_total_teachers()
        users = func.getAllUsers()
        print(users)
        return render_template("dashboard_admin.html", data = {"users":users,"stats":[total_users, total_students, total_teachers]} )
    else:
        return render_template("login.html", error_message = "you must log in first")

@admin.route('/students')
def students():
    if ('email' in session and session['profile'] == 'admin'):
        total_users = func.get_total_users()
        total_students = func.get_total_students()
        total_teachers = func.get_total_teachers()
        students = func.getAllStudents()
        return render_template('students_admin.html', data = {"users":students,"stats":[total_users, total_students, total_teachers]} )
    else:
        return render_template("students_admin.html", error_message = "You must log in first")
    
@admin.route('/add_student', methods=['POST','GET'])
def add_students():
    if ('email' in session and session['profile'] == 'admin'):
        if request.method == 'POST':
            name = request.form['nom']
            surname = request.form['prenom']
            email = request.form['email']
            password = request.form['password']
            profile = 'student'
            status = 'offline'
            grade = request.form['classe']
            id_user = func.generate_ID_Student()
            # user = student(id_user, name, surname, email, password, profile, status, grade)
            adder = func.getAdminByEmail(session['email'])
            
            result = adder.add_user(id_user, name, surname, email, password, profile, status, grade)
            users = func.getAllStudents()
            total_users = func.get_total_users()
            total_students = func.get_total_students()
            total_teachers = func.get_total_teachers()
            if result[0]:
                flash('Student added successfully')
                print(func.getAllStudents)
                return render_template("students_admin.html", data = {"users":users,"stats":[total_users, total_students, total_teachers]} )
            else:
                flash('Failed to add student')
                return render_template("students_admin.html", data = {"error_message":result[1],"users":users,"stats":[total_users, total_students, total_teachers]})
        else:
            return render_template('students_admin.html', data = {"error_message":result[1],"users":users,"stats":[total_users, total_students, total_teachers]})