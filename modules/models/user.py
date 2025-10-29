from datetime import datetime, timezone

from sqlalchemy import ForeignKey

from modules.settings.database import db
from modules.models.user_type import UserType


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), index=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=True)
    user_type = db.Column(db.Integer, ForeignKey("user_type.id"))
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime)

    type = db.relationship("UserType", backref="users", lazy="joined")

    def update(self, data: dict[str, str]):
        for key, value in data.items():
            setattr(self, key, value)
