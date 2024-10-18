from models.db import db
from sqlalchemy_serializer import SerializerMixin
class OrderItem(db.Model,SerializerMixin):
    __tablename__ = 'order_items'

    serialize_rules = ('-order', '-product',)

    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Integer, nullable = False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column(db.Integer,db.ForeignKey('products.id'))

    order = db.relationship('Order', back_populates = 'order_items')
    product = db.relationship('Product', back_populates = 'order_items')
    