# Workout API

A backend REST API for a workout tracking application built for personal trainers. The API handles workouts and exercises, allowing trainers to create workouts, manage exercises, and associate exercises with specific workouts.

Built with Flask, SQLAlchemy, and Marshmallow.

---

## Tech Stack

- Python 3.8+
- Flask 2.2.2
- Flask-SQLAlchemy 3.0.3
- Flask-Migrate 3.1.0
- Marshmallow 3.20.1
- SQLite (via instance/workout.db)
- Pipenv

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/jareelireri-ops/workout-api.git
cd workout-api
```

**2. Install dependencies**
```bash
pipenv install
pipenv shell
```

**3. Set up the database**
```bash
flask db upgrade
```

**4. Seed the database**
```bash
python seed.py
```

**5. Run the application**
```bash
python run.py
```

The server will start at `http://localhost:5000`

---

## API Endpoints

### Workouts

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/workouts` | Get all workouts |
| GET | `/workouts/<id>` | Get a single workout by ID (includes nested exercises) |
| POST | `/workouts` | Create a new workout |
| PATCH | `/workouts/<id>` | Update a workout |
| DELETE | `/workouts/<id>` | Delete a workout |

### Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/exercises` | Get all exercises |
| GET | `/exercises/<id>` | Get a single exercise by ID |
| POST | `/exercises` | Create a new exercise |
| DELETE | `/exercises/<id>` | Delete an exercise |

### Workout Exercises

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/workout_exercises` | Add an exercise to a workout (with sets, reps, or duration) |

---

## Project Structure

```
workout-api/
├── app/
│   ├── models/
│   │   ├── workout.py
│   │   ├── exercise.py
│   │   └── workout_exercise.py
│   ├── routes/
│   │   ├── workout_routes.py
│   │   └── exercise_routes.py
│   ├── schemas/
│   │   ├── workout_schema.py
│   │   ├── exercise_schema.py
│   │   └── workout_exercise_schema.py
│   └── config.py
├── migrations/
├── instance/
│   └── workout.db
├── seed.py
├── run.py
└── Pipfile

#DEV
Jareelireri-ops

## Author

Jareel Ireri — [@jareelireri-ops](https://github.com/jareelireri-ops)
