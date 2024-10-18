from models.db import db
from sqlalchemy_serializer import SerializerMixin

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    serialize_rules = ('-user', '-order_items',)

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    address = db.Column(db.String, nullable=False)
    status = db.Column(db.String, nullable=False)

    user = db.relationship('User', back_populates='orders')
    order_items = db.relationship('OrderItem', back_populates='order', cascade="all, delete-orphan")
