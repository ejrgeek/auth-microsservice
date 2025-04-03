from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from .model import User
from .extensions import db
from .jwt_utils import generate_token

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    
    if not data.get("username") or not data.get("password"):
        return jsonify({"error": "Username and password required"}), 400
    
    if User.query.filter_by(username=data["username"]).first():
        # Credenciais já existentes, mas quem cria conta não precisa
        # ter o conhecimento de que o nome de usuario ja existe,
        # então aqui deve retornar outra mensagem
        return jsonify({"error": "Username already exists"}), 409
        
    hashed_password = generate_password_hash(
        data["password"],
        method="pbkdf2:sha256",
        salt_length=16
    )
    
    new_user = User(username=data["username"], password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
        
    token, expires_in = generate_token(new_user.id)
    return jsonify({
        "message": "User created!",
        "token": token,
        "expires_in": expires_in.total_seconds()
    }), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token, expires_in = generate_token(user.id)
    return jsonify({
        "token": token,
        "expires_in": expires_in.total_seconds()
    }), 200
