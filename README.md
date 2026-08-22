# Techiva — MVP

Flow: **Home → Login/Register → Grade Selection → Game Path → Lesson (image + quiz)**

A Duolingo-style take on the grade-based learning flow: each grade is a
winding path of lesson nodes. Nodes unlock one at a time as you complete the
one before it, each lesson has a custom illustration, a simple + technical
explanation, and a one-question quiz that awards XP and builds a daily streak.

## Project structure

```
techiva/
├── app.py                # routes: home, register, login, select-grade, knowledge (path), lesson
├── models.py               # User (XP/streak) + Progress (per-lesson completion)
├── content.py               # grade-wise lesson data incl. quiz questions (swap for a DB table later)
├── config.py                # SECRET_KEY, DB URI (reads from env vars if set)
├── requirements.txt
├── templates/
│   ├── base.html              # nav, XP/streak pills, flash messages
│   ├── home.html
│   ├── register.html
│   ├── login.html
│   ├── select_grade.html
│   ├── knowledge.html          # the game path for a grade
│   └── lesson.html              # single lesson + quiz
└── static/
    ├── css/style.css
    └── images/icons/*.svg       # hand-built illustrations (Arduino, ESP32, sensors, robot, etc.)
```

## Gamification model

- **XP**: 20 XP per lesson, awarded once (re-answering doesn't double it).
- **Streak**: increments once per calendar day the student completes a
  lesson; resets if a day is skipped. Shown as a 🔥 pill in the nav.
- **Locking**: the first lesson in a grade is always open; each next one
  unlocks only after the previous is completed. Direct URL access to a
  locked lesson redirects back to the path.
- **Progress bar**: shown at the top of the path, computed from completed
  lessons ÷ total lessons for that grade.

## Setup

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 — the SQLite DB (`techiva.db`) is created
automatically on first run.

## How the flow works

1. **Home** (`/`) — public landing page.
2. **Register / Login** (`/register`, `/login`) — creates a `User` row with a
   hashed password (`werkzeug.security`), logs them in with Flask-Login.
3. **Grade Selection** (`/select-grade`) — student picks 3rd–10th standard;
   saved on `User.grade`. Required before viewing the path.
4. **Game Path** (`/knowledge/<grade>`) — a winding column of lesson nodes.
   Each node's state (locked / active / completed) is computed from the
   `Progress` table on every request — nothing is pre-baked, so completing a
   lesson immediately unlocks the next node.
5. **Lesson** (`/lesson/<grade>/<topic_id>`) — shows the illustration, the
   **Simple Explanation**, a collapsible **Technical Explanation**, then a
   one-question quiz. A correct answer creates/updates a `Progress` row,
   calls `User.award_xp_and_streak()`, and sends the student back to the path.

## Extending this

- **Move content to the DB**: replace `content.py`'s dict with a `Topic`
  model (`grade`, `title`, `icon`, `image`, `simple`, `technical`, and a
  related `QuizQuestion` model) and change `get_topics_for_grade()` /
  `get_topic()` to queries. Routes don't need to change.
- **More quiz questions per lesson**: `topic["quiz"]` is currently one
  question; turn it into a list and loop over it in `lesson.html` + tally
  a score in the `lesson()` view.
- **Badges**: add a `Badge`/`StudentBadge` model and check thresholds (e.g.
  "first lesson", "5-day streak") inside `award_xp_and_streak()`.
- **Admin panel**: add a `role` column to `User`, gate an `/admin` blueprint
  with `@login_required` + a role check, and let admins CRUD the `Topic` table.
- **More sections** (projects library, engineering explorer, teacher/parent
  dashboards): each can be its own blueprint following the same pattern — a
  model, a `routes.py`, and templates that extend `base.html`.

## Note on the illustrations

The board/sensor/robot images in `static/images/icons/` are hand-drawn SVG
illustrations (not photos) — this keeps the app fully self-contained with no
external image links that could break, and matches the flat, playful style
of game-based learning apps. Swap any of them for real photos later by
changing the `image` filename per topic in `content.py`.

## Notes

- Passwords are hashed with Werkzeug's `generate_password_hash` — never
  stored in plain text.
- `SECRET_KEY` and `DATABASE_URL` can be overridden via environment
  variables for production; defaults are fine for local dev.
