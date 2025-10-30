from datetime import datetime, timezone

from models.user import User
from models.user_type import UserType
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import Session


def seed_data(session: Session):
    if not UserType.query.first():
        manager_type = UserType(user_type="manager")
        employee_type = UserType(user_type="employee")
        session.add_all([manager_type, employee_type])
        session.commit()

    if not User.query.first():
        manager_type = UserType.query.filter_by(user_type="manager").first()
        user = User(
            name="Admin",
            username="admin",
            email="admin@admin.com",
            password=generate_password_hash("admin"),
            user_type=manager_type.id,
            created_at=datetime.now(timezone.utc),
            created_by=1
        )
        session.add(user)
        session.commit()
