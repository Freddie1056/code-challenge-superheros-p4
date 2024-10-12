from flask import request, jsonify
from flask_restful import Resource
from models import Hero, db

class HeroResource(Resource):
    def get(self):
        heroes = Hero.query.all()
        return jsonify([hero.to_dict() for hero in heroes]), 200

    def post(self):
        data = request.get_json()
        if not data.get('name') or not data.get('super_name'):
            return {"error": "Both name and super_name are required."}, 400
        new_hero = Hero(name=data['name'], super_name=data['super_name'])
        db.session.add(new_hero)
        db.session.commit()
        return {"message": "Hero created successfully!"}, 201
