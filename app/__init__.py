import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_wtf.csrf import CSRFProtect
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = os.path.abspath('./uploads/')
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app, origins=['http://localhost:2921'])

from app import views