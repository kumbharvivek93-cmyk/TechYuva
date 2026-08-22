from datetime import date, datetime, timedelta

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()

XP_PER_LESSON = 20


class User(UserMixin, db.Model):
    """A registered student account."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    # Grade the student picked after login. Null until they choose one.
    grade = db.Column(db.Integer, nullable=True)

    # --- Gamification ---
    xp = db.Column(db.Integer, default=0, nullable=False)
    streak = db.Column(db.Integer, default=0, nullable=False)
    last_activity = db.Column(db.Date, nullable=True)  # last day XP was earned

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    progress_entries = db.relationship(
        "Progress", backref="user", lazy=True, cascade="all, delete-orphan"
    )

    def set_password(self, raw_password: str) -> None:
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password: str) -> bool:
        return check_password_hash(self.password_hash, raw_password)

    def completed_topic_ids(self, grade: int):
        """Set of topic ids this user has completed for a given grade."""
        return {
            p.topic_id
            for p in self.progress_entries
            if p.grade == grade and p.completed
        }

    def award_xp_and_streak(self, amount: int = XP_PER_LESSON) -> None:
        """Add XP and update the daily learning streak."""
        self.xp += amount
        today = date.today()
        if self.last_activity == today:
            pass  # already counted today, don't double the streak
        elif self.last_activity == today - timedelta(days=1):
            self.streak += 1
            self.last_activity = today
        else:
            self.streak = 1
            self.last_activity = today

    def __repr__(self):
        return f"<User {self.username} grade={self.grade} xp={self.xp}>"


class Progress(db.Model):
    """Tracks whether a student has completed a specific lesson."""

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    topic_id = db.Column(db.String(80), nullable=False)
    completed = db.Column(db.Boolean, default=False, nullable=False)
    completed_at = db.Column(db.DateTime, nullable=True)

    __table_args__ = (
        db.UniqueConstraint("user_id", "grade", "topic_id", name="uq_user_grade_topic"),
    )

    def __repr__(self):
        return f"<Progress user={self.user_id} {self.grade}/{self.topic_id} completed={self.completed}>"
