"""
TECHIVA — MVP Flask app (gamified, Duolingo-style).

Flow:
    Home  ->  Register/Login  ->  Grade Selection  ->  Grade Path (game map)
    ->  Lesson (image + explanation + quiz)  ->  back to Path (unlocks next node)

Run with:  python app.py
Then open: http://127.0.0.1:5000
"""

from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

from config import Config
from content import (PROJECTS, SENSORS, get_available_grades, get_development_boards,
                     get_topic, get_topics_for_grade)
from models import Progress, User, db

# ---------------------------------------------------------------------------
# App + extension setup
# ---------------------------------------------------------------------------
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Please log in to continue."
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@app.route("/")
def home():
    """Public landing page."""
    return render_template("home.html")


THEMES = {
    "jungle": {"name": "Jungle Explorer", "icon": "🌴", "description": "Discover technology in the wild."},
    "game": {"name": "Game World", "icon": "🎮", "description": "Level up one mission at a time."},
    "neon": {"name": "Neon Future", "icon": "⚡", "description": "Explore the world of future technology."},
    "space": {"name": "Space Engineer", "icon": "🚀", "description": "Build ideas beyond the stars."},
    "lab": {"name": "Science Lab", "icon": "🔬", "description": "Experiment, observe and invent."},
    "workshop": {"name": "Engineering Workshop", "icon": "🛠️", "description": "Turn parts into prototypes."},
}


@app.context_processor
def inject_theme():
    return {"active_theme": session.get("theme", "jungle"), "themes": THEMES}


@app.route("/theme", methods=["POST"])
def set_theme():
    theme = request.form.get("theme", "jungle")
    if theme in THEMES:
        session["theme"] = theme
        flash(f"{THEMES[theme]['name']} theme selected!", "success")
    return redirect(request.referrer or url_for("home"))


@app.route("/dashboard")
@login_required
def dashboard():
    grades = get_available_grades()
    completed = sum(len(current_user.completed_topic_ids(grade)) for grade in grades)
    total = sum(len(get_topics_for_grade(grade)) for grade in grades)
    next_topic = None
    if current_user.grade in grades:
        for topic in get_topics_for_grade(current_user.grade):
            if topic["id"] not in current_user.completed_topic_ids(current_user.grade):
                next_topic = topic
                break
    badges = [
        ("🌟 First Explorer", completed >= 1), ("⚡ Circuit Starter", completed >= 3),
        ("📡 Sensor Scout", completed >= 5), ("🤖 Robot Builder", completed >= 8),
    ]
    return render_template("dashboard.html", completed=completed, total=total,
                           next_topic=next_topic, badges=badges)


@app.route("/board-lab")
def board_lab():
    """Kid-friendly introduction to popular development boards."""
    return render_template("board_lab.html", boards=get_development_boards())


@app.route("/boards")
def boards():
    return render_template("boards.html", boards=get_development_boards())


@app.route("/sensors")
def sensors():
    return render_template("sensors.html", sensors=SENSORS)


@app.route("/sensors/hc-sr04")
def ultrasonic_sensor():
    return render_template("hc_sr04.html")


@app.route("/projects")
@app.route("/build-lab")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/projects/<project_id>")
def project_detail(project_id):
    project = next((item for item in PROJECTS if item["id"] == project_id), None)
    if project is None:
        flash("That project is not in the lab yet.", "error")
        return redirect(url_for("projects"))
    return render_template("project_detail.html", project=project)


@app.route("/learn")
def learn():
    return render_template("learn.html")


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    results = []
    if query:
        for item in get_development_boards() + SENSORS + PROJECTS:
            haystack = " ".join(str(value) for value in item.values()).lower()
            if query in haystack:
                results.append(item)
    return render_template("search.html", query=query, results=results)


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("select_grade"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        error = None
        if not username or not email or not password:
            error = "All fields are required."
        elif password != confirm:
            error = "Passwords do not match."
        elif len(password) < 6:
            error = "Password must be at least 6 characters."
        elif User.query.filter_by(username=username).first():
            error = "That username is already taken."
        elif User.query.filter_by(email=email).first():
            error = "An account with that email already exists."

        if error:
            flash(error, "error")
            return render_template("register.html", username=username, email=email)

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash(f"Welcome to Techiva, {user.username}!", "success")
        return redirect(url_for("select_grade"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("select_grade"))

    if request.method == "POST":
        identifier = request.form.get("identifier", "").strip()
        password = request.form.get("password", "")

        user = User.query.filter(
            (User.username == identifier) | (User.email == identifier.lower())
        ).first()

        if user and user.check_password(password):
            login_user(user)
            flash(f"Welcome back, {user.username}!", "success")
            if user.grade:
                return redirect(url_for("knowledge", grade=user.grade))
            return redirect(url_for("select_grade"))

        flash("Invalid username/email or password.", "error")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "success")
    return redirect(url_for("home"))


@app.route("/select-grade", methods=["GET", "POST"])
@login_required
def select_grade():
    grades = get_available_grades()

    if request.method == "POST":
        grade = request.form.get("grade", type=int)
        if grade not in grades:
            flash("Please select a valid grade.", "error")
            return render_template("select_grade.html", grades=grades)

        current_user.grade = grade
        db.session.commit()
        return redirect(url_for("knowledge", grade=grade))

    return render_template("select_grade.html", grades=grades)


@app.route("/knowledge")
@app.route("/knowledge/<int:grade>")
@login_required
def knowledge(grade=None):
    grades = get_available_grades()

    # Default to the student's saved grade if none was passed in the URL.
    if grade is None:
        grade = current_user.grade

    if grade not in grades:
        flash("Please select your grade first.", "error")
        return redirect(url_for("select_grade"))

    topics = get_topics_for_grade(grade)
    completed_ids = current_user.completed_topic_ids(grade)

    # Build the game path: each node knows if it's completed, unlocked, or locked.
    # Rule: the first node is always unlocked; every later node unlocks once
    # the node right before it has been completed.
    nodes = []
    previous_completed = True
    for topic in topics:
        is_completed = topic["id"] in completed_ids
        nodes.append({
            "topic": topic,
            "completed": is_completed,
            "unlocked": previous_completed,
        })
        previous_completed = is_completed

    completed_count = len(completed_ids)
    total_count = len(topics)
    progress_pct = int((completed_count / total_count) * 100) if total_count else 0

    return render_template(
        "knowledge.html",
        grade=grade,
        grades=grades,
        nodes=nodes,
        completed_count=completed_count,
        total_count=total_count,
        progress_pct=progress_pct,
    )


@app.route("/lesson/<int:grade>/<topic_id>", methods=["GET", "POST"])
@login_required
def lesson(grade, topic_id):
    topic = get_topic(grade, topic_id)
    if topic is None:
        flash("That lesson doesn't exist.", "error")
        return redirect(url_for("select_grade"))

    # Lock check: don't allow jumping straight to a locked lesson via URL.
    topics = get_topics_for_grade(grade)
    completed_ids = current_user.completed_topic_ids(grade)
    topic_index = next(i for i, t in enumerate(topics) if t["id"] == topic_id)
    is_unlocked = topic_index == 0 or topics[topic_index - 1]["id"] in completed_ids
    already_completed = topic_id in completed_ids

    if not is_unlocked and not already_completed:
        flash("Complete the previous lesson first!", "error")
        return redirect(url_for("knowledge", grade=grade))

    feedback = None  # "correct" | "incorrect" | None

    if request.method == "POST":
        selected = request.form.get("answer", type=int)
        correct_index = topic["quiz"]["correct"]

        if selected == correct_index:
            feedback = "correct"
            progress = Progress.query.filter_by(
                user_id=current_user.id, grade=grade, topic_id=topic_id
            ).first()
            if progress is None:
                progress = Progress(user_id=current_user.id, grade=grade, topic_id=topic_id)
                db.session.add(progress)
            if not progress.completed:
                progress.completed = True
                progress.completed_at = db.func.now()
                current_user.award_xp_and_streak()
            db.session.commit()
        else:
            feedback = "incorrect"

    return render_template(
        "lesson.html",
        grade=grade,
        topic=topic,
        feedback=feedback,
        already_completed=already_completed,
    )


# ---------------------------------------------------------------------------
# CLI helper: create DB tables on first run
# ---------------------------------------------------------------------------
@app.cli.command("init-db")
def init_db():
    """Run with: flask --app app.py init-db"""
    with app.app_context():
        db.create_all()
    print("Database initialized.")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # convenient for local dev; creates techiva.db if missing
    app.run(debug=True)
