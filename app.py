from flask import Flask, request, make_response, jsonify, session
from flask_migrate import Migrate
from flask_restful import Resource, Api
from datetime import datetime
from models.db import db
from models.order import Order
from models.order_item import OrderItem
from models.product import Product
from models.user import User
from flask_cors import CORS
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dukashop:duka_app@localhost/dukadb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)
app.secret_key = 'your_secret_key'  
bcrypt = Bcrypt(app)

migrate = Migrate(app, db)
db.init_app(app)

api = Api(app)

# Users Resource
class UsersResource(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return make_response(jsonify(users), 200)

    def post(self):
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return make_response(jsonify(new_user.to_dict()), 201)

api.add_resource(UsersResource, '/users')

class UserByID(Resource):
    def get(self, id):
        user = User.query.filter_by(id=id).first()

        if user is None:
            return make_response({"error": "User not found"}, 404)

        response_dict = user.to_dict()

        response = make_response(
            response_dict,
            200,
        )

        return response
    

    def patch(self, id):
        record = User.query.filter_by(id=id).first()
        for attr in request.form:
            setattr(record, attr, request.form[attr])
        db.session.add(record)
        db.session.commit()
        return make_response(record.to_dict(), 200)

    def delete(self, id):
        record = User.query.filter_by(id=id).first()
        db.session.delete(record)
        db.session.commit()
        return make_response({"message": "record successfully deleted"}, 200)

api.add_resource(UserByID, '/users/<int:id>')

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'password' not in data:
            return make_response({'message': 'Missing required fields'}, 400)

        existing_user = User.query.filter_by(email=data['email']).first()
        if existing_user:
            return make_response({'message': 'User already exists'}, 400)

        new_user = User(name=data['name'], email=data['email'])
        new_user.password = data['password']  # Use the setter to hash the password
        db.session.add(new_user)
        db.session.commit()

        return make_response(jsonify(new_user.to_dict()), 201)

api.add_resource(UserRegistration, '/register')

class Login(Resource):
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['user_id'] = user.id
            return {'name': user.name, 'id': user.id}, 200
        return {'message': 'Invalid email or password'}, 401

api.add_resource(Login, '/login')

class Logout(Resource):
    def delete(self):
        session.pop('user_id', None)
        return '', 204

api.add_resource(Logout, '/logout')

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = User.query.get(user_id)
            return {'name': user.name, 'id': user.id, 'email': user.email}, 200
        return {}, 401

api.add_resource(CheckSession, '/check_session')

class ProductResource(Resource):
    def get(self):
        products = Product.query.all()
        return make_response(jsonify([product.to_dict() for product in products]), 200)

    def post(self):
        data = request.get_json()
        new_product = Product(name=data['name'], price=data['price'], description=data['description'], image=data['image'])
        db.session.add(new_product)
        db.session.commit()
        return make_response(jsonify(new_product.to_dict()), 201)

api.add_resource(ProductResource, '/products')

class ProductByID(Resource):
    def get(self, id):
        response_dict = Product.query.filter_by(id=id).first().to_dict()
        return make_response(response_dict, 200)

    def patch(self, id):
        product = Product.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(product, key, value)
        db.session.commit()
        return make_response(product.to_dict(), 200)

    def delete(self, id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return make_response({'message': 'Product deleted'}, 200)

api.add_resource(ProductByID, '/products/<int:id>')

class OrderResource(Resource):
    def get(self):
        orders = Order.query.all()
        return make_response(jsonify([order.to_dict() for order in orders]), 200)

    def post(self):
        data = request.get_json()
        new_order = Order(date=datetime.utcnow(), user_id=data['user_id'], address=data['address'], status=data['status'])
        db.session.add(new_order)
        db.session.commit()
        return make_response(jsonify(new_order.to_dict()), 201)

api.add_resource(OrderResource, '/orders')

class OrderByID(Resource):
    def get(self, id):
        response_dict = Order.query.filter_by(id=id).first().to_dict()
        return make_response(response_dict, 200)

    def delete(self, id):
        record = Order.query.filter_by(id=id).first()
        db.session.delete(record)
        db.session.commit()
        return make_response({"message": "Order successfully deleted"}, 200)

api.add_resource(OrderByID, '/orders/<int:id>')

class OrderItemResource(Resource):
    def get(self):
        order_items = OrderItem.query.all()
        return make_response(jsonify([order_item.to_dict() for order_item in order_items]), 200)

    def post(self):
        data = request.get_json()
        new_order_item = OrderItem(quantity=data['quantity'], order_id=data['order_id'], product_id=data['product_id'])
        db.session.add(new_order_item)
        db.session.commit()
        return make_response(jsonify(new_order_item.to_dict()), 201)

api.add_resource(OrderItemResource, '/order_items')

class OrderItemByID(Resource):
    def get(self, id):
        order_item = OrderItem.query.filter_by(id=id).first()
        if not order_item:
            return make_response({'message': 'Order item not found'}, 404)
        return make_response(jsonify(order_item.to_dict()), 200)

    def delete(self, id):
        order_item = OrderItem.query.filter_by(id=id).first()
        if not order_item:
            return make_response({'message': 'Order item not found'}, 404)
        db.session.delete(order_item)
        db.session.commit()
        return make_response({'message': 'Order item deleted'}, 200)

api.add_resource(OrderItemByID, '/order_items/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
