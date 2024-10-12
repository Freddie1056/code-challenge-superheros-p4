from flask_restful import Resource
from flask import jsonify, request
from models import HeroPower, db

class HeroPowerResource(Resource):
    def get(self):
        hero_powers = HeroPower.query.all()
        return jsonify([hp.to_dict() for hp in hero_powers]), 200

    def post(self):
        data = request.get_json()
        if not data.get('hero_id') or not data.get('power_id'):
            return {"error": "Both hero_id and power_id are required."}, 400
        new_hero_power = HeroPower(hero_id=data['hero_id'], power_id=data['power_id'])
        db.session.add(new_hero_power)
        db.session.commit()
        return {"message": "Hero power created successfully!"}, 201
