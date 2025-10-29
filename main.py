from flask import Flask
from flask_migrate import Migrate

from modules.exceptions.handler.exception_handler import add_exception_handler
from modules.resources.routers.user_routes import user_apis
from modules.settings.database import db
from modules.settings.database import get_database_url

app = Flask(__name__)

migrate = Migrate()

app.config['SQLALCHEMY_DATABASE_URI'] = get_database_url()
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()
migrate.init_app(app, db)

app.register_blueprint(user_apis, url_prefix='/users')

add_exception_handler(app)

if __name__ == '__main__':
    app.run(debug=True)
