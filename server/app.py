from flask import request, session, jsonify
from flask_restful import Resource
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from config import app, db, bcrypt, api
from models import User, Episode, Appearance, Guest

jwt = JWTManager(app)

class Register(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return {'error': 'Username and password required'}, 400

        if User.query.filter_by(username=username).first():
            return {'error': 'Username already exists'}, 400

        new_user = User(
            username=username,
            _password_hash=bcrypt.generate_password_hash(password.encode('utf-8')).decode('utf-8')
        )
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201

class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if not user or not bcrypt.check_password_hash(user._password_hash, password.encode('utf-8')):
            return {'error': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200

class Episodes(Resource):
    def get(self):
        episodes = Episode.query.all()
        return [episode.to_dict() for episode in episodes], 200

class EpisodeById(Resource):
    def get(self, id):
        episode = Episode.query.get(id)
        if not episode:
            return {'error': 'Episode not found'}, 404
        return episode.to_dict(), 200

    @jwt_required()
    def delete(self, id):
        current_user_id = get_jwt_identity()
        episode = Episode.query.get(id)
        
        if not episode:
            return {'error': 'Episode not found'}, 404
        
        try:
            db.session.delete(episode)
            db.session.commit()
            return {'message': 'Episode deleted'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

class Guests(Resource):
    def get(self):
        guests = Guest.query.all()
        return [guest.to_dict() for guest in guests], 200

class Appearances(Resource):
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        data = request.get_json()
        
        required_fields = ['rating', 'guest_id', 'episode_id']
        if not all(field in data for field in required_fields):
            return {'error': 'Missing required fields'}, 400
        
        try:
            new_appearance = Appearance(
                rating=data['rating'],
                guest_id=data['guest_id'],
                episode_id=data['episode_id']
            )
            db.session.add(new_appearance)
            db.session.commit()
            return new_appearance.to_dict(), 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400

api.add_resource(Register, '/register')
api.add_resource(Login, '/login')
api.add_resource(Episodes, '/episodes')
api.add_resource(EpisodeById, '/episodes/<int:id>')
api.add_resource(Guests, '/guests')
api.add_resource(Appearances, '/appearances')

if __name__ == '__main__':
    app.run(debug=True)