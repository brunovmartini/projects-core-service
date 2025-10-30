from functools import wraps

from flask_login import current_user, login_required
from werkzeug.exceptions import Forbidden


def manager_required(f):
    @wraps(f)
    @login_required
    def decorated_function(*args, **kwargs):
        if getattr(current_user, "user_type", None) != 1:
            raise Forbidden()
        return f(*args, **kwargs)

    return decorated_function
