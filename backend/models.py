from flask_marshmallow import Marshmallow
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import (create_access_token,
                                create_refresh_token,
                                jwt_required,
                                get_jwt_identity)
from datetime import datetime
db = SQLAlchemy()
ma = Marshmallow()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120), nullable = False)

    def __init__(self, username, password):
        self.username = username
        self.password = User.generate_hash(password)

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)
    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

class UserSchema(ma.Schema):
    class Meta:
        fields = ('username', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    cost = db.Column(db.Float, nullable = False)
    state = db.Column(db.String(120), nullable = False)
    info = db.Column(db.String(120),nullable = False)
    brand = db.Column(db.String(120),nullable = False)
    newCost = db.Column(db.Float, nullable = False)

class ItemSchema(ma.Schema):
    class Meta:
        fields = ('name', 'cost', 'state', 'info','brand','newCost','id')

item_schema = ItemSchema()
items_schema = ItemSchema(many=True)

class DepositItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    deposit = db.Column(db.Float, nullable = False)
    state = db.Column(db.String(120), nullable = False)
    info = db.Column(db.String(120),nullable = False)
    brand = db.Column(db.String(120),nullable = False)
    expiry_date = db.Column(db.DateTime,nullable = False)

class DepositItemSchema(ma.Schema):
    days_left = fields.Method("calculate_days_left")
    def calculate_days_left(self, obj):
        return (obj.expiry_date - datetime.now()).days
    class Meta:
        fields = ('name', 'deposit', 'state', 'info','brand','days_left','id')

deposit_item_schema = DepositItemSchema()
deposit_items_schema = DepositItemSchema(many=True)
class RevokedTokenModel(db.Model):
    __tablename__ = 'revoked_tokens'
    id = db.Column(db.Integer, primary_key = True)
    jti = db.Column(db.String(120))

    def add(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def is_jti_blacklisted(cls, jti):
        query = cls.query.filter_by(jti = jti).first()
        return bool(query)
