import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "postgresql://auth_user:senha_segura@localhost/auth_db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")
    JWT_ACCESS_TOKEN_EXPIRES = 2592000
    #JWT_COOKIE_SECURE = True  # PERMITE APENAS HTTPS
    #JWT_COOKIE_SAMESITE = "Lax"  # FLAG DE PROTEÇÃO CSRF
