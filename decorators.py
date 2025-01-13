from functools import wraps
from flask import redirect, url_for, flash
from flask_login import current_user

def roles_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for('login'))
            if current_user.role not in roles:
                flash("Vous n'avez pas l'autorisation d'accéder à cette page.", 'error')
                return redirect(url_for('index'))
            return f(*args, **kwargs)
        return decorated_view
    return wrapper