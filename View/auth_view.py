from datetime import timedelta
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from models import User

auth_db = Blueprint('auth', __name__)

@auth_db.route("/login", methods=['POST'])
def login():
    # Asegúrate de que se obtengan los datos de autorización correctamente
    data = request.authorization
    username = data.username 
    password = data.password

    usuario = User.query.filter_by(username=username).first()
    
    if usuario and check_password_hash(
        pwhash=usuario.password_hash, password=password
    ):
        access_token = create_access_token(
            identity=username,
            expires_delta=timedelta(minutes=10),
            additional_claims=dict(
                administrador=usuario.is_admin
            ),
        )
        return jsonify({'Token': f'Bearer {access_token}'})

    return jsonify(Mensaje="El usuario y la contraseña al parecer no coinciden")
