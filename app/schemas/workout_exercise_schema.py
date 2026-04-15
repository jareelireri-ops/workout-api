from app import ma
from app.models.workout_exercise import WorkoutExercise

class WorkoutExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise
        load_instance = True
        include_fk = True
    
    # Just show the exercise details, don't try to nest anything deeper
    exercise = ma.Nested("ExerciseSchema")

workout_exercise_schema = WorkoutExerciseSchema()
workout_exercises_schema = WorkoutExerciseSchema(many=True)