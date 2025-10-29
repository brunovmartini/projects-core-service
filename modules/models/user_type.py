from modules.settings.database import db


class UserType(db.Model):
    __tablename__ = 'user_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type = db.Column(db.String(8), nullable=False)
