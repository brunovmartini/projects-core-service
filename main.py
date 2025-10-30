import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from exceptions.exception_handler import add_exception_handler
from models.user import User
from models.user_type import UserType
from models.project import Project
from models.task import Task
from resources.routers.auth_routes import auth_apis
from resources.routers.project_routes import project_apis
from resources.routers.user_routes import user_apis
from settings.database import db
from settings.database import get_database_url
from settings.seed import seed_data

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev-secret-key")

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


migrate = Migrate()

app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()
    seed_data()
migrate.init_app(app, db)

app.register_blueprint(user_apis, url_prefix='/users')
app.register_blueprint(project_apis, url_prefix='/projects')
app.register_blueprint(auth_apis, url_prefix="/auth")

add_exception_handler(app)

if __name__ == '__main__':
    app.run(debug=True)
