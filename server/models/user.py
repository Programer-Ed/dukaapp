# from models.db import db
# from sqlalchemy_serializer import SerializerMixin
# from sqlalchemy.ext.hybrid import hybrid_property
# from flask_bcrypt import Bcrypt

# bcrypt = Bcrypt()

# class User(db.Model,SerializerMixin):

#     __tablename__ = 'users'

#     serialize_rules = ('-orders', '-carts',)

#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(50), nullable = False, unique =True)
#     email= db.Column(db.String(255), nullable = False, unique = True)
#     _password_hash = db.Column(db.String, nullable=False)

#     orders = db.relationship('Order', back_populates = 'user')


#     @hybrid_property
#     def password(self):
#         return self._password_hash

#     @password.setter
#     def password(self, password):
#         self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

#     def check_password(self, password):
#         return bcrypt.check_password_hash(self._password_hash, password)

from models.db import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    serialize_rules = ('-orders',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    _password_hash = db.Column(db.String, nullable=False)

    orders = db.relationship('Order', back_populates='user')

    @hybrid_property
    def password(self):
        return self._password_hash

    @password.setter
    def password(self, password):
        self._password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self._password_hash, password)
