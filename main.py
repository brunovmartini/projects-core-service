from flask import Flask
from flask_migrate import Migrate

from exceptions.exception_handler import add_exception_handler
from resources.routers.user_routes import user_apis
from resources.routers.project_routes import project_apis
from settings.database import db
from settings.database import get_database_url
from settings.seed import seed_data

app = Flask(__name__)

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

add_exception_handler(app)

if __name__ == '__main__':
    app.run(debug=True)
