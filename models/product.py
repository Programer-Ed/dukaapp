from models.db import db
from sqlalchemy_serializer import SerializerMixin
class Product(db.Model,SerializerMixin):
    __tablename__ = 'products'

    serialize_rules = ('-order_items',)

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),nullable = False, unique = True)
    description = db.Column(db.String,nullable = True)
    image = db.Column(db.String,nullable = True)
    price = db.Column(db.Float, nullable = False)

    order_items = db.relationship('OrderItem', back_populates = 'product')

    def __repr__(self):
        return f'<Product {self.name}, Price: {self.price}>'

