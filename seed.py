import psycopg2
from psycopg2.extras import execute_values
from faker import Faker
import random
from datetime import timedelta

# Configuration de la connexion à la base de données
conn = psycopg2.connect(
    dbname='schoolproject',         # Remplacez par le nom de votre base de données
    user='root',         # Remplacez par votre utilisateur PostgreSQL
    password='postGres',  # Remplacez par votre mot de passe
    host='localhost',
    port='5432'
)
cur = conn.cursor()
faker = Faker('fr_FR')

# 1. Génération des écoles
schools = [(faker.company(), faker.address()) for _ in range(5)]
execute_values(cur, "INSERT INTO schools (name, address) VALUES %s RETURNING id;", schools)
school_ids = [row[0] for row in cur.fetchall()]
conn.commit()

# 2. Génération des classes pour chaque école avec des niveaux fixes et des suffixes aléatoires
class_levels = ["6eme", "5eme", "4eme", "3eme"]
suffixes = ["A", "B", "C"]  # Possibilités de suffixes
classes = []
for school_id in school_ids:
    for level in class_levels:
        # Créer 1 ou 2 classes par niveau pour simuler différentes sections (ex: 6A, 6B)
        nb_classes = random.randint(1, 2)
        for _ in range(nb_classes):
            suffix = random.choice(suffixes)
            classes.append((f"{level}{suffix}", school_id))
execute_values(cur, "INSERT INTO classes (name, school_id) VALUES %s RETURNING id;", classes)
class_ids = [row[0] for row in cur.fetchall()]
conn.commit()

# 3. Génération des matières fixes pour chaque école
fixed_subjects = [
    "Mathematiques", "francais", "anglais",
    "histoire", "geographie", "eps",
    "svt", "education civique"
]
subjects = []
for school_id in school_ids:
    for subject in fixed_subjects:
        subjects.append((subject, school_id))
execute_values(cur, "INSERT INTO subjects (name, school_id) VALUES %s RETURNING id;", subjects)
subject_ids = [row[0] for row in cur.fetchall()]
conn.commit()

# 4. Génération des utilisateurs (students, teachers, admins)
users = []
roles = ['student', 'teacher', 'admin']
# Créer plus d'élèves que de professeurs et d'administrateurs
for role in roles:
    nb = 20 if role == 'student' else 5
    for _ in range(nb):
        school_id = random.choice(school_ids)
        # Pour les élèves, associer une classe au hasard parmi celles de l'école
        if role == 'student':
            # On filtre les classes de l'école choisie
            possible_classes = [cid for cid, sch in zip(class_ids, [school_id]*len(class_ids)) if True]
            # Ici, pour simplifier, on choisit une classe au hasard dans toutes les classes (à améliorer en filtrant par school_id)
            class_id = random.choice(class_ids)
        else:
            class_id = None
        users.append((
            faker.unique.email(),
            faker.password(length=10),  # Idéalement, on hashera ce mot de passe
            faker.first_name(),
            faker.last_name(),
            role,
            school_id,
            class_id
        ))
execute_values(cur,
    """
    INSERT INTO users (email, password_hash, first_name, last_name, role, school_id, class_id)
    VALUES %s RETURNING id, role;
    """,
    users
)
user_rows = cur.fetchall()
conn.commit()

# Séparation des utilisateurs par rôle pour les données associées
students = [uid for uid, role in user_rows if role == 'student']
teachers = [uid for uid, role in user_rows if role == 'teacher']
admins   = [uid for uid, role in user_rows if role == 'admin']

# 5. Génération des bulletins/notes pour les étudiants
grades = []
for student_id in students:
    nb_notes = random.randint(3, 8)
    for _ in range(nb_notes):
        teacher_id = random.choice(teachers) if teachers else None
        subject_id = random.choice(subject_ids)
        score = round(random.uniform(0, 20), 2)
        date_note = faker.date_between(start_date='-1y', end_date='today')
        comment = faker.sentence(nb_words=10)
        grades.append((student_id, teacher_id, subject_id, score, date_note, comment))
execute_values(cur,
    """
    INSERT INTO grades (student_id, teacher_id, subject_id, score, date, comments)
    VALUES %s;
    """,
    grades
)
conn.commit()

# 6. Génération des emplois du temps pour enseignants et administrateurs
schedules = []
for user_id in teachers + admins:
    nb_events = random.randint(2, 5)
    for _ in range(nb_events):
        event = faker.sentence(nb_words=4)
        start_time = faker.date_time_between(start_date='-30d', end_date='now')
        end_time = start_time + timedelta(hours=random.randint(1, 3))
        schedules.append((user_id, event, start_time, end_time))
execute_values(cur,
    """
    INSERT INTO schedules (user_id, event, start_time, end_time)
    VALUES %s;
    """,
    schedules
)
conn.commit()

# 7. Génération des feedbacks pour les étudiants
feedbacks = []
for student_id in students:
    nb_feedback = random.randint(1, 3)
    for _ in range(nb_feedback):
        comment = faker.text(max_nb_chars=100)
        date_feedback = faker.date_between(start_date='-6m', end_date='today')
        feedbacks.append((student_id, comment, date_feedback))
execute_values(cur,
    """
    INSERT INTO feedback (student_id, comment, date)
    VALUES %s;
    """,
    feedbacks
)
conn.commit()

# 8. Génération des rendez-vous pour les administrateurs
appointments = []
for admin_id in admins:
    nb_appointments = random.randint(1, 4)
    for _ in range(nb_appointments):
        title = f"RDV {faker.word().capitalize()}"
        description = faker.sentence(nb_words=8)
        date_appointment = faker.date_time_between(start_date='-30d', end_date='+30d')
        appointments.append((admin_id, title, description, date_appointment))
execute_values(cur,
    """
    INSERT INTO appointments (admin_id, title, description, date)
    VALUES %s;
    """,
    appointments
)
conn.commit()

cur.close()
conn.close()

print("Insertion des données fictives terminée.")
