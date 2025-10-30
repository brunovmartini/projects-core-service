from datetime import datetime, timezone

from models.user import User
from models.user_type import UserType
from settings.database import db
from werkzeug.security import generate_password_hash


def seed_data():
    if not UserType.query.first():
        manager_type = UserType(user_type="manager")
        employee_type = UserType(user_type="employee")
        db.session.add_all([manager_type, employee_type])
        db.session.commit()

    if not User.query.first():
        manager_type = UserType.query.filter_by(user_type="manager").first()
        user = User(
            name="Admin",
            username="admin",
            email="admin@admin.com",
            password=generate_password_hash("admin"),
            user_type=manager_type.id,
            created_at=datetime.now(timezone.utc)
        )
        db.session.add(user)
        db.session.commit()
