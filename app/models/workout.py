from app import db
from sqlalchemy.orm import validates

class Workout(db.Model):
    __tablename__ = 'workouts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    date = db.Column(db.String)

    workout_exercises = db.relationship('WorkoutExercise', backref='workout', cascade="all, delete-orphan")

    @validates('title')
    def validate_title(self, key, title):
        if not title:
            raise ValueError("Workout must have a title.")
        return title