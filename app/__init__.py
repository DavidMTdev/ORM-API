from flask import Flask
from app import config
from app.models import db
from app.controller import user, post, message, fixtures

app = Flask(__name__)
app.config.from_object(config.Config)

app.register_blueprint(user.main)
app.register_blueprint(post.post)
app.register_blueprint(message.message)
app.register_blueprint(fixtures.fixtures)

db.init_app(app)

# with app.app_context():
