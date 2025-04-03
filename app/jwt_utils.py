from flask import current_app
from flask_jwt_extended import create_access_token
from datetime import timedelta

def generate_token(user_id):
    token = create_access_token(identity=user_id)
    expires_in = timedelta(seconds=current_app.config['JWT_ACCESS_TOKEN_EXPIRES'])
    return token, expires_in