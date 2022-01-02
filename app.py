from flask_restful import Api
from flask_migrate import Migrate
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager

from backend.models import db, ma

# APP + DB
app = Flask(__name__)
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

from backend.resources import UserLogin,AllUsers,UserRegistration,UserLogoutAccess, SecretResource

api.add_resource(UserRegistration, '/registration')
api.add_resource(AllUsers, '/users')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogoutAccess, '/logout')
api.add_resource(SecretResource, '/secret')

if __name__ == "__main__":
    app.run(debug=True)
    