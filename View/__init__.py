from .auth_view import auth_db

def register_db(app):
    app.register_blueprint(auth_db)