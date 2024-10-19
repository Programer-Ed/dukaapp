from models.db import db
from models.user import User
from models.order import Order
from models.order_item import OrderItem
from models.product import Product
from app import app
from datetime import datetime
from faker import Faker
import random

faker = Faker()


def clear_database():
    with app.app_context():
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()
        db.session.query(Product).delete()
        db.session.query(User).delete()
        db.session.commit()


clear_database()


users = [{
    "name": faker.name(),
    "email": faker.unique.email(),  
    "password": faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
} for _ in range(10)]

with app.app_context():
 
    for user_data in users:
        new_user = User(**user_data)
        db.session.add(new_user)

    db.session.commit()


    products = []
    product_names = set() 
    while len(products) < 10:
        product_name = faker.word()
        if product_name not in product_names:
            product_names.add(product_name)
            product_data = {
                "name": product_name,
                "price": round(random.uniform(5, 500), 2),
                "description": faker.sentence(),
                "image": random.choice([
                    "https://d16zmt6hgq1jhj.cloudfront.net/product/10916/Manji%20Choco%20Chip%20Cookies%20500g.jpg",
                    "https://d16zmt6hgq1jhj.cloudfront.net/product/11022/Millbakers%20Heart%20Deli%20750g.jpg",
                    "https://d16zmt6hgq1jhj.cloudfront.net/product/10029/Daima%20Esl%20Fresh%20Milk%20500Ml.jpg",
                    "https://d16zmt6hgq1jhj.cloudfront.net/product/1421/Fresh%20Red%20Seedless%20Grapes%20500G.jpg",
                    "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/01/009419/1.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/h55/h58/16871976566814/13866_1.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/h7d/hbd/50866627182622/194745_main.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/hcc/h2b/16930286338078/9014_main.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/h33/h3e/16930287353886/9006_main.jpg",
                    "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/98/572685/1.jpg",
                ])
            }
            products.append(product_data)


    for product_data in products:
        new_product = Product(**product_data)
        db.session.add(new_product)


    db.session.commit()


    order_status = ["Pending", "Shipped", "Delivered"]
    orders = []

    user_ids = [user.id for user in User.query.all()]
    
    for _ in range(10):
        order_data = {
            "user_id": random.choice(user_ids),  
            "date": datetime.utcnow(),
            "address": faker.address(),
            "status": random.choice(order_status)
        }
        new_order = Order(**order_data)
        db.session.add(new_order)
        orders.append(new_order)  


    db.session.commit()


    product_ids = [product.id for product in Product.query.all()]

    for order in orders:
        for _ in range(random.randint(1, 5)):
            order_item = OrderItem(
                quantity=random.randint(1, 20),
                order_id=order.id,
                product_id=random.choice(product_ids)  
            )
            db.session.add(order_item)


    db.session.commit()
