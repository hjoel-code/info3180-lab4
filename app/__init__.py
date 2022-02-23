from flask import Flask
from .config import Config


from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect()

app = Flask(__name__)
csrf.init_app(app)


app.config.from_object(Config)
from app import views
