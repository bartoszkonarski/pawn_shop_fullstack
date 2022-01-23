from flask_restful import Api
from flask_migrate import Migrate
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from backend.models import db, ma

# APP + DB
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///backend/database.db'
db.init_app(app)
ma.init_app(app)
with app.app_context():
    db.create_all()


# jwt
app.config['JWT_TOKEN_LOCATION'] = ['headers', 'query_string']
app.config['JWT_SECRET_KEY'] = 'jwt-secret-string'
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access'] # ['access', 'refresh']

jwt = JWTManager(app)

api = Api(app)

from backend.resources import AddItem,TransferExpiredItems,AllDepositItems,SingleDepositItem,AddDepositItem, AllItems, SingleItem, UserLogin,AllUsers,UserRegistration,UserLogoutAccess, SecretResource

api.add_resource(UserRegistration, '/registration')
api.add_resource(AllUsers, '/users')
api.add_resource(AllItems, '/items')
api.add_resource(AllDepositItems, '/deposit_items')
api.add_resource(AddItem, '/item')
api.add_resource(AddDepositItem, '/deposit_item')
api.add_resource(SingleItem, '/item/<int:item_id>')
api.add_resource(SingleDepositItem, '/deposit_item/<int:deposit_item_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout')
api.add_resource(SecretResource, '/secret')
api.add_resource(TransferExpiredItems,'/sell_expired')

if __name__ == "__main__":
    app.run(debug=True)
    