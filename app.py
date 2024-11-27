from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instancia que se usará para definir los modelos
db = SQLAlchemy()
print("Se creó una instancia db")

def create_app():
    app = Flask(__name__, template_folder="templates")

    # configuramos la URL 
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:postgres@localhost:5432/flaskdb"

    # Vincula la instancia de sqlalchemy con flask
    db.init_app(app)

    from routes import register_routes
    register_routes(app, db)

    migrate = Migrate(app, db)

    return app