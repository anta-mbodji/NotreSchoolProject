from flask import Blueprint, request, jsonify
import psycopg2
from config import get_db_connection

notes_bp = Blueprint("notes_bp", __name__)

@notes_bp.route("/notes", methods=["GET"])
def get_notes():
    """Récupérer toutes les notes"""
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM notes")
    notes = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([
        {"id": note[0], "student_id": note[1], "subject_id": note[2], "score": note[3], "date": note[4].strftime("%Y-%m-%d")}
        for note in notes
    ])

@notes_bp.route("/notes", methods=["POST"])
def add_note():
    """Ajouter une nouvelle note"""
    data = request.json
    student_id = data.get("student_id")
    subject_id = data.get("subject_id")
    score = data.get("score")

    if not all([student_id, subject_id, score]):
        return jsonify({"error": "Tous les champs sont requis"}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO notes (student_id, subject_id, score) VALUES (%s, %s, %s) RETURNING id",
            (student_id, subject_id, score),
        )
        note_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"message": "Note ajoutée avec succès !", "note_id": note_id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
