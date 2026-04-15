from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.json.compact = False 
    
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    # Model Imports
    from app.models.exercise import Exercise
    from app.models.workout import Workout
    from app.models.workout_exercise import WorkoutExercise

    # Schema Imports
    from app.schemas.exercise_schema import exercise_schema
    from app.schemas.workout_schema import workout_schema
    from app.schemas.workout_exercise_schema import workout_exercise_schema

    # Route Registrations
    from app.routes.exercise_routes import exercise_bp
    from app.routes.workout_routes import workout_bp
    
    app.register_blueprint(exercise_bp)
    app.register_blueprint(workout_bp)

    return app