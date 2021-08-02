from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from elasticsearch import Elasticsearch


db = SQLAlchemy()
migrate = Migrate()
bootstrap = Bootstrap()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)
        bootstrap.init_app(app)

        app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
            if app.config['ELASTICSEARCH_URL'] else None
            
        from app.main import bp as main_bp
        app.register_blueprint(main_bp)
    
        
    return app

from app import models

