from app import ma
from app.models.workout import Workout

class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout
        load_instance = True
        include_fk = True

    # Show the exercises associated with the workout
    workout_exercises = ma.Nested("WorkoutExerciseSchema", many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)