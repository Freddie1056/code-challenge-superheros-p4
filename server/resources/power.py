from flask_restful import Resource
from flask import jsonify, request
from models import Power, db

class PowerResource(Resource):
    def get(self):
        powers = Power.query.all()
        return jsonify([power.to_dict() for power in powers]), 200

    def post(self):
        data = request.get_json()
        if not data.get('name') or not data.get('description'):
            return {"error": "Both name and description are required."}, 400
        new_power = Power(name=data['name'], description=data['description'])
        db.session.add(new_power)
        db.session.commit()
        return {"message": "Power created successfully!"}, 201
