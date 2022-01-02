from flask_restful import Resource
from flask import request
from backend.models import db, User, user_schema, users_schema, RevokedTokenModel
from flask_jwt_extended import jwt_required, create_access_token, get_jwt
from datetime import timedelta

class UserRegistration(Resource):
    def post(self):
        username = request.json['username']
        password = request.json['password']

        new_user = User(username, password)

        #try:
        db.session.add(new_user)
        db.session.commit()

        access_token = create_access_token(identity = request.json['username'], expires_delta=timedelta(days=30))
        return {
                'message': 'User {} was created'.format(request.json['username']),
                'access_token': access_token
                }

class AllUsers(Resource):
    @jwt_required()
    def get(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        all_users = User.query.all()
        result = users_schema.dump(all_users)
        return result

    # def delete(self):
    #     return {'message': 'Delete all users'}


class UserLogin(Resource):
    def post(self):
        current_user = User.find_by_username(request.json['username'])
        if not current_user: # remove this for security issue.
            return {'message': 'User {} doesn\'t exist'.format(request.json['username'])}

        if User.verify_hash(request.json['password'], current_user.password):
            access_token = create_access_token(identity = request.json['username'], expires_delta=timedelta(days=30))
            return {
                    'message': 'Logged in as {}'.format(current_user.username),
                    'access_token': access_token
                    }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        try:
            revoked_token = RevokedTokenModel(jti = jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class SecretResource(Resource):
    @jwt_required()
    def get(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        else:
            return {'answer': 42}