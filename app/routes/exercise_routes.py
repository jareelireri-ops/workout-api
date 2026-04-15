from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.exercise import Exercise
from app.schemas.exercise_schema import exercise_schema, exercises_schema

# Create a Blueprint , which is the way we organize our routes in Flask.
#  This allows us to group related routes together
exercise_bp = Blueprint('exercise_bp', __name__)

# GEt ALL EXERCISES
@exercise_bp.route('/exercises', methods=['GET'])
def get_exercises():
    exercises = Exercise.query.all()
    return make_response(exercises_schema.dump(exercises), 200)

# GET A SINGLE EXERCISE BY ID
@exercise_bp.route('/exercises/<int:id>', methods=['GET'])
def get_exercise(id):
    exercise = Exercise.query.get(id)
    if not exercise:
        return make_response(jsonify({"error": "Exercise not found"}), 404)
    return make_response(exercise_schema.dump(exercise), 200)

# POST to CREATE A NEW EXERCISE
@exercise_bp.route('/exercises', methods=['POST'])
def create_exercise():
    data = request.get_json()
    try:
        new_exercise = exercise_schema.load(data, session=db.session)
        db.session.add(new_exercise)
        db.session.commit()
        return make_response(exercise_schema.dump(new_exercise), 201)
    except Exception as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)