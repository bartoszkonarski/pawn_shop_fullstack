from flask_restful import Resource
from flask import request
from backend.models import Item, db, User, user_schema, users_schema, RevokedTokenModel, items_schema
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
            return {'message': 'User {} doesn\'t exist'.format(request.json['username'])},404

        if User.verify_hash(request.json['password'], current_user.password):
            access_token = create_access_token(identity = request.json['username'], expires_delta=timedelta(days=30))
            return {
                    'message': 'Logged in as {}'.format(current_user.username),
                    'access_token': access_token
                    }
        else:
            return {'message': 'Wrong credentials'},404


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


class AllItems(Resource):
    @jwt_required()
    def get(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        all_items = Item.query.all()
        result = items_schema.dump(all_items)
        return result

class GetItem(Resource):
    @jwt_required()
    def get(self, item_id):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        result = Item.query.filter_by(id=item_id)
        return items_schema.dump(result)

    @jwt_required()
    def delete(self, item_id):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
            
        try:
            Item.query.filter_by(id=item_id).delete()
            db.session.commit()
            return {'message': f'Item: {item_id} succesfully deleted'}
        except:
            return {'message': 'Something went wrong'}, 500


class AddItem(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        try:
            item = Item(name = request.json['name'],
                        cost = float(request.json['cost']),
                        state = request.json['state'],
                        info = request.json['info'],
                        brand = request.json['brand'],
                        newCost = float(request.json['newCost'])
                    )
            db.session.add(item)
            db.session.commit()
            return {'message': 'Item added successfully'}
        except:
            return {'message': 'Something went wrong'}, 500