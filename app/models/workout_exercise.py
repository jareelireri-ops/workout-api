from app import db
from sqlalchemy.orm import validates

class WorkoutExercise(db.Model):
    __tablename__ = 'workout_exercises'

    id = db.Column(db.Integer, primary_key=True)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercises.id'), nullable=False)
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)

    @validates('reps', 'sets')
    def validate_counts(self, key, value):
        if value is not None and value <= 0:
            raise ValueError(f"{key} must be a positive number.")
        return value