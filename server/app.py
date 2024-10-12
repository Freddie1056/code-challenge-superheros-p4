from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

# Import configurations and models
from config import Config
from models import db

# Import resources
from resources.hero import HeroResource
from resources.power import PowerResource
from resources.hero_power import HeroPowerResource

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS
CORS(app)

# Initialize the database and migrations
db.init_app(app)
migrate = Migrate(app, db)

# Set up Flask-RESTful API
api = Api(app)

# Root endpoint
@app.route('/')
def index():
    return '<h1>Superheroes API</h1>'

# Register resources with their respective routes
api.add_resource(HeroResource, '/heroes')
api.add_resource(PowerResource, '/powers')
api.add_resource(HeroPowerResource, '/hero_powers')

# Run the app
if __name__ == '__main__':
    app.run(port=5555, debug=True)
