# Habit Tracker

A straightforward CLI backend to track habits, streaks, and analytics, built with Python and SQLite.

Developed as part of my **Fundamentals of Programming** course.

---

## Features

- **Simple CLI**: Clean menu to create, modify, check off, and delete habits.
- **Custom periodicity**: Support for daily, weekly, or any custom day interval.
- **Analytics**: Calculates streaks and highlights which habits you're struggling with most.
- **SQLite storage**: Lightweight local database (`main.db`) to keep history intact.
- **Flexible check-ins**: Check off habits for today or log previous dates.

---

## Setup

Python 3's standard library handles almost everything. To run the tests, install `pytest`:

```bash
pip install pytest
```

---

## How to Run

- **Start with a fresh database**:
  ```bash
  python main.py
  ```

- **Load demo data first (optional)**:
  If you want sample habits and historical check-ins loaded:
  ```bash
  python predefined_data.py
  python main.py
  ```

---

## Testing

Tests run against an isolated `test.db`, so your `main.db` won't be touched:

```bash
pytest test_habit_tracker.py
```

---

### Author
Eric Ristol
