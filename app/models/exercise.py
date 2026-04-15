from app import db
from sqlalchemy.orm import validates

# This model represents an exercise that can be included in workouts. 
# Each exercise has a name and an optional description.
class Exercise(db.Model):
    __tablename__ = 'exercises'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String)

    workout_exercises = db.relationship('WorkoutExercise', backref='exercise', cascade="all, delete-orphan")

    @validates('name')
    def validate_name(self, key, name):
        if not name or len(name) < 3:
            raise ValueError("Exercise name must be at least 3 characters long.")
        return name