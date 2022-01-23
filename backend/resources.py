from flask_restful import Resource
from flask import request
from backend.models import (Item, 
                            db, 
                            User, 
                            users_schema, 
                            RevokedTokenModel, 
                            items_schema,
                            DepositItem,
                            deposit_items_schema
)
from flask_jwt_extended import jwt_required, create_access_token, get_jwt
from datetime import datetime, timedelta

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

class SingleItem(Resource):
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
    
    @jwt_required()
    def put(self,item_id):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403

        item = Item.query.filter_by(id=item_id).first()
        item.name = request.json['name']
        item.cost = float(request.json['cost'])
        item.state = request.json['state']
        item.info = request.json['info']
        item.brand = request.json['brand']
        item.newCost = float(request.json['newCost'])
        
        db.session.commit()
        return {'message': f'Item: {item_id} succesfully edited'}

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
    
class AllDepositItems(Resource):
    @jwt_required()
    def get(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        all_items = DepositItem.query.all()
        result = deposit_items_schema.dump(all_items)
        return result

class SingleDepositItem(Resource):
    @jwt_required()
    def get(self, deposit_item_id):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        result = DepositItem.query.filter_by(id=deposit_item_id)
        return deposit_items_schema.dump(result)

    @jwt_required()
    def delete(self, deposit_item_id):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
            
        try:
            DepositItem.query.filter_by(id=deposit_item_id).delete()
            db.session.commit()
            return {'message': f'Item: {deposit_item_id} succesfully deleted'}
        except:
            return {'message': 'Something went wrong'}, 500
    
class AddDepositItem(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        try:
            time_change = timedelta(days=30)
            expiry_dt = datetime.now() + time_change
            item = DepositItem(name = request.json['name'],
                        deposit = float(request.json['deposit']),
                        state = request.json['state'],
                        info = request.json['info'],
                        brand = request.json['brand'],
                        expiry_date = expiry_dt
                    )
            db.session.add(item)
            db.session.commit()
            return {'message': 'Item added successfully'}
        except:
            return {'message': 'Something went wrong'}, 500

class TransferExpiredItems(Resource):
    @jwt_required()
    def patch(self):
        jti = get_jwt()['jti']
        if RevokedTokenModel.is_jti_blacklisted(jti):
            return {'message': 'Access Denied'}, 403
        
        try:
            for deposit_item in DepositItem.query.all():
                if deposit_item.expiry_date<=datetime.now():
                    item = Item(name = deposit_item.name,
                            cost = float(deposit_item.deposit),
                            state = deposit_item.state,
                            info = deposit_item.info,
                            brand = deposit_item.brand,
                            newCost = float(deposit_item.deposit*1.3)
                        )
                    db.session.add(item)
                    DepositItem.query.filter_by(id=deposit_item.id).delete()
                    db.session.commit()
            return {'message': 'Expired deposit items have been marked as available for sale'}
        except:
            return {'message': 'Something went wrong'}, 500