from flask import Flask
from flask_migrate import Migrate
from app.routes import employee_bp
from app.database import db
import os

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

    db.init_app(app)
    migrate.init_app(app, db)
    
    app.register_blueprint(employee_bp)
    
    with app.app_context():
        db.create_all()
    
    return app