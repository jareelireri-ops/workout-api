from app import ma
from app.models.exercise import Exercise

class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise
        load_instance = True
        include_fk = True

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)