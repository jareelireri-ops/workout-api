from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.workout import Workout
from app.schemas.workout_schema import workout_schema, workouts_schema

workout_bp = Blueprint('workout_bp', __name__)

# GET ALL WORKOUTS
@workout_bp.route('/workouts', methods=['GET'])
def get_workouts():
    workouts = Workout.query.all()
    return make_response(workouts_schema.dump(workouts), 200)

# GET ONE WORKOUT BY ID. 
# this will also include the exercises nested,meaning, 
# when we get a workout, we will also see the exercises that are part of that workout.
@workout_bp.route('/workouts/<int:id>', methods=['GET'])
def get_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({"error": "Workout not found"}), 404)
    return make_response(workout_schema.dump(workout), 200)

# PATCH (UPDATE) A WORKOUT
@workout_bp.route('/workouts/<int:id>', methods=['PATCH'])
def update_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({"error": "Workout not found"}), 404)
    
    data = request.get_json()
    try:
        # This is a simple way to update the workout with any fields provided in the request.
        for attr in data:
            setattr(workout, attr, data[attr])
        
        db.session.commit()
        return make_response(workout_schema.dump(workout), 200)
    except Exception as e:
        return make_response(jsonify({"errors": [str(e)]}), 400)

# DELETE A WORKOUT
@workout_bp.route('/workouts/<int:id>', methods=['DELETE'])
def delete_workout(id):
    workout = Workout.query.get(id)
    if not workout:
        return make_response(jsonify({"error": "Workout not found"}), 404)
    
    db.session.delete(workout)
    db.session.commit()
    return make_response(jsonify({"message": "Workout deleted successfully"}), 204)