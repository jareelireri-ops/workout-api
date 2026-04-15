from app import create_app, db
from app.models.workout import Workout
from app.models.exercise import Exercise
from app.models.workout_exercise import WorkoutExercise

app = create_app()

with app.app_context():
    print("Clearing old data...")
    WorkoutExercise.query.delete()
    Workout.query.delete()
    Exercise.query.delete()

    print("Seeding exercises...")
    ex1 = Exercise(name="Pushups", description="Standard floor pushups")
    ex2 = Exercise(name="Squats", description="Bodyweight squats")
    ex3 = Exercise(name="Plank", description="Core stability hold")
    db.session.add_all([ex1, ex2, ex3])

    print("Seeding workouts...")
    w1 = Workout(title="Morning Blast", date="2026-04-15")
    w2 = Workout(title="Leg Day", date="2026-04-16")
    db.session.add_all([w1, w2])
    db.session.commit() # Commit here so we have IDs for the next step

    print("Linking exercises to workouts...")
    # Add Pushups to Morning Blast
    we1 = WorkoutExercise(workout_id=w1.id, exercise_id=ex1.id, reps=20, sets=3)
    # Add Squats to Leg Day
    we2 = WorkoutExercise(workout_id=w2.id, exercise_id=ex2.id, reps=15, sets=4)
    
    db.session.add_all([we1, we2])
    db.session.commit()

    print("Database seeded successfully! You're ready for the 100.")