from flask import Flask
from .extensions import db, jwt
from ..config import Config
from .routes import auth_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    jwt.init_app(app)
    
    with app.app_context():
        app.register_blueprint(auth_bp, url_prefix='/api/auth')
        
        from sqlalchemy import text
        with db.engine.begin() as connection:
            connection.execute(text("CREATE SCHEMA IF NOT EXISTS auth_schema"))
        db.create_all()
    
    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)