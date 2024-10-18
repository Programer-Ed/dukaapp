# from models.db import db
# from models.user import User
# from models.order import Order
# from models.order_item import OrderItem
# from models.product import Product
# from app import app
# from datetime import datetime
# from faker import Faker
# import random

# faker = Faker()

# # Function to clear the database
# def clear_database():
#     with app.app_context():
#         db.session.query(OrderItem).delete()
#         db.session.query(Order).delete()
#         db.session.query(Product).delete()
#         db.session.query(User).delete()
#         db.session.commit()

# # Clear the database before seeding
# clear_database()

# # Generate random users
# users = [{
#     "name": faker.name(),
#     "email": faker.email(),
#     "password": faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
# } for _ in range(100)]

# # List of product images
# product_images = [
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/10916/Manji%20Choco%20Chip%20Cookies%20500g.jpg",
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/11022/Millbakers%20Heart%20Deli%20750g.jpg",
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/10029/Daima%20Esl%20Fresh%20Milk%20500Ml.jpg",
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/1421/Fresh%20Red%20Seedless%20Grapes%20500G.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/01/009419/1.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/h55/h58/16871976566814/13866_1.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/h7d/hbd/50866627182622/194745_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/hcc/h2b/16930286338078/9014_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/h33/h3e/16930287353886/9006_main.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/98/572685/1.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/81/0345581/1.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/75/070023/1.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/ha3/h4a/16871923089438/1294_main.jpg", 
#     "https://cdn.mafrservices.com/sys-master-root/h75/h9e/16930270969886/1494_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/hb2/hcc/16975373893662/43271_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/hed/h9a/51543114711070/211073_main.jpg", 
#     "https://img.freepik.com/premium-photo/bottle-milk-some-blueberries-table_662214-455559.jpg",
#     "https://img.freepik.com/free-photo/three-bottles-beer_23-2148600945.jpg",
#     "https://img.freepik.com/free-photo/backet-with-toilet-paper-rolls_23-2148550627.jpg",
#     "https://img.freepik.com/premium-photo/three-eggs-brown-eggs-are-shown-with-water-droplets-them_978914-17758.jpg",
#     "https://img.freepik.com/free-photo/ingredient-bags-full-flour_23-2149482567.jpg",
#     "https://img.freepik.com/free-photo/black-white-cookies-package_140725-4381.jpg",
#     "https://img.freepik.com/premium-photo/selection-artisanal-bread-rolls-including-whole-grain-ciabatta_1327465-40806.jpg",
#     "https://img.freepik.com/premium-photo/stack-cheese-that-says-butter-it_1126605-1937.jpg",
#     "https://img.freepik.com/premium-photo/dettol-soap-picture-dettol-soap-white-background-with-selective-focus_1197797-245618.jpg",
#     "https://img.freepik.com/premium-photo/set-3d-bottles-with-oil_1299086-964.jpg" 
# ]

# # Generate random products
# products = [{
#     "name": faker.word(),
#     "price": round(random.uniform(5, 500), 2),
#     "description": faker.sentence(),
#     "image": random.choice(product_images)
# } for _ in range(100)]

# # Use the application context to perform database operations
# with app.app_context():
#     # Create users
#     for user_data in users:
#         new_user = User(**user_data)
#         db.session.add(new_user)

#     # Create products
#     for product_data in products:
#         existing_product = db.session.query(Product).filter_by(name=product_data['name']).first()
#         if not existing_product:
#             new_product = Product(**product_data)
#             db.session.add(new_product)

#     # Commit the changes to the database
#     db.session.commit()

#     # Create orders
#     order_status = ["Pending", "Shipped", "Delivered"]
#     orders = [{
#         "user_id": random.randint(1, 100),
#         "date": datetime.utcnow(),
#         "address": faker.address(),
#         "status": random.choice(order_status)
#     } for _ in range(50)]

#     for order_data in orders:
#         new_order = Order(**order_data)
#         db.session.add(new_order)

#     # Create order items
#     order_items = [{
#         "quantity": random.randint(1, 20),
#         "order_id": random.randint(1, 50),
#         "product_id": random.randint(1, 100)
#     } for _ in range(100)]

#     for order_item_data in order_items:
#         new_order_item = OrderItem(**order_item_data)
#         db.session.add(new_order_item)

#     # Commit all changes to the database
#     db.session.commit()

# from models.db import db
# from models.user import User
# from models.order import Order
# from models.order_item import OrderItem
# from models.product import Product
# from app import app
# from datetime import datetime
# from faker import Faker
# import random

# faker = Faker()

# # Function to clear the database
# def clear_database():
#     with app.app_context():
#         db.session.query(OrderItem).delete()
#         db.session.query(Order).delete()
#         db.session.query(Product).delete()
#         db.session.query(User).delete()
#         db.session.commit()

# # Clear the database before seeding
# clear_database()

# # Generate random users
# users = [{
#     "name": faker.name(),
#     "email": faker.unique.email(),  # Ensures unique emails
#     "password": faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
# } for _ in range(100)]

# # List of product images
# product_images = [
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/10916/Manji%20Choco%20Chip%20Cookies%20500g.jpg",
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/11022/Millbakers%20Heart%20Deli%20750g.jpg",
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/10029/Daima%20Esl%20Fresh%20Milk%20500Ml.jpg",
#     "https://d16zmt6hgq1jhj.cloudfront.net/product/1421/Fresh%20Red%20Seedless%20Grapes%20500G.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/01/009419/1.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/h55/h58/16871976566814/13866_1.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/h7d/hbd/50866627182622/194745_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/hcc/h2b/16930286338078/9014_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/h33/h3e/16930287353886/9006_main.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/98/572685/1.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/81/0345581/1.jpg",
#     "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/75/070023/1.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/ha3/h4a/16871923089438/1294_main.jpg", 
#     "https://cdn.mafrservices.com/sys-master-root/h75/h9e/16930270969886/1494_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/hb2/hcc/16975373893662/43271_main.jpg",
#     "https://cdn.mafrservices.com/sys-master-root/hed/h9a/51543114711070/211073_main.jpg", 
#     "https://img.freepik.com/premium-photo/bottle-milk-some-blueberries-table_662214-455559.jpg",
#     "https://img.freepik.com/free-photo/three-bottles-beer_23-2148600945.jpg",
#     "https://img.freepik.com/free-photo/backet-with-toilet-paper-rolls_23-2148550627.jpg",
#     "https://img.freepik.com/premium-photo/three-eggs-brown-eggs-are-shown-with-water-droplets-them_978914-17758.jpg",
#     "https://img.freepik.com/free-photo/ingredient-bags-full-flour_23-2149482567.jpg",
#     "https://img.freepik.com/free-photo/black-white-cookies-package_140725-4381.jpg",
#     "https://img.freepik.com/premium-photo/selection-artisanal-bread-rolls-including-whole-grain-ciabatta_1327465-40806.jpg",
#     "https://img.freepik.com/premium-photo/stack-cheese-that-says-butter-it_1126605-1937.jpg",
#     "https://img.freepik.com/premium-photo/dettol-soap-picture-dettol-soap-white-background-with-selective-focus_1197797-245618.jpg",
#     "https://img.freepik.com/premium-photo/set-3d-bottles-with-oil_1299086-964.jpg" 
# ]

# # Use the application context to perform database operations
# with app.app_context():
#     # Create users
#     for user_data in users:
#         new_user = User(**user_data)
#         db.session.add(new_user)

#     # Commit the users to the database
#     db.session.commit()

#     # Generate random products, avoiding duplicates
#     products = []
#     product_names = set()  # To track unique product names
#     while len(products) < 100:
#         product_name = faker.word()
#         if product_name not in product_names:
#             product_names.add(product_name)
#             product_data = {
#                 "name": product_name,
#                 "price": round(random.uniform(5, 500), 2),
#                 "description": faker.sentence(),
#                 "image": random.choice(product_images)
#             }
#             products.append(product_data)

#     # Create products
#     for product_data in products:
#         new_product = Product(**product_data)
#         db.session.add(new_product)

#     # Commit the changes to the database
#     db.session.commit()

#     # Create orders
#     order_status = ["Pending", "Shipped", "Delivered"]
#     orders = []
#     for _ in range(50):
#         order_data = {
#             "user_id": random.randint(1, 100),  # Random user from the created users
#             "date": datetime.utcnow(),
#             "address": faker.address(),
#             "status": random.choice(order_status)
#         }
#         new_order = Order(**order_data)
#         db.session.add(new_order)
#         orders.append(new_order)  # Store the created orders

#     # Commit the orders to the database
#     db.session.commit()

#     # Create order items
#     for order in orders:
#         for _ in range(random.randint(1, 5)):  # Random number of items per order
#             order_item = OrderItem(
#                 quantity=random.randint(1, 20),
#                 order_id=order.id,
#                 product_id=random.randint(1, len(products))  # Use valid product IDs from the product list
#             )
#             db.session.add(order_item)

#     # Commit all changes to the database
#     db.session.commit()

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

# Function to clear the database
def clear_database():
    with app.app_context():
        db.session.query(OrderItem).delete()
        db.session.query(Order).delete()
        db.session.query(Product).delete()
        db.session.query(User).delete()
        db.session.commit()

# Clear the database before seeding
clear_database()

# Generate random users
users = [{
    "name": faker.name(),
    "email": faker.unique.email(),  # Ensures unique emails
    "password": faker.password(length=8, special_chars=True, digits=True, upper_case=True, lower_case=True)
} for _ in range(100)]

# Use the application context to perform database operations
with app.app_context():
    # Create users
    for user_data in users:
        new_user = User(**user_data)
        db.session.add(new_user)

    # Commit the users to the database
    db.session.commit()

    # Generate random products, avoiding duplicates
    products = []
    product_names = set()  # To track unique product names
    while len(products) < 100:
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
                    "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/81/0345581/1.jpg",
                    "https://ke.jumia.is/unsafe/fit-in/680x680/filters:fill(white)/product/75/070023/1.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/ha3/h4a/16871923089438/1294_main.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/h75/h9e/16930270969886/1494_main.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/hb2/hcc/16975373893662/43271_main.jpg",
                    "https://cdn.mafrservices.com/sys-master-root/hed/h9a/51543114711070/211073_main.jpg",
                    "https://img.freepik.com/premium-photo/bottle-milk-some-blueberries-table_662214-455559.jpg",
                    "https://img.freepik.com/free-photo/three-bottles-beer_23-2148600945.jpg",
                    "https://img.freepik.com/free-photo/backet-with-toilet-paper-rolls_23-2148550627.jpg",
                    "https://img.freepik.com/premium-photo/three-eggs-brown-eggs-are-shown-with-water-droplets-them_978914-17758.jpg",
                    "https://img.freepik.com/free-photo/ingredient-bags-full-flour_23-2149482567.jpg",
                    "https://img.freepik.com/free-photo/black-white-cookies-package_140725-4381.jpg",
                    "https://img.freepik.com/premium-photo/selection-artisanal-bread-rolls-including-whole-grain-ciabatta_1327465-40806.jpg",
                    "https://img.freepik.com/premium-photo/stack-cheese-that-says-butter-it_1126605-1937.jpg",
                    "https://img.freepik.com/premium-photo/dettol-soap-picture-dettol-soap-white-background-with-selective-focus_1197797-245618.jpg",
                    "https://img.freepik.com/premium-photo/set-3d-bottles-with-oil_1299086-964.jpg"
                ])
            }
            products.append(product_data)

    # Create products
    for product_data in products:
        new_product = Product(**product_data)
        db.session.add(new_product)

    # Commit the changes to the database
    db.session.commit()

    # Create orders
    order_status = ["Pending", "Shipped", "Delivered"]
    orders = []
    
    # Fetch user IDs to use for order creation
    user_ids = [user.id for user in User.query.all()]
    
    for _ in range(50):
        order_data = {
            "user_id": random.choice(user_ids),  # Random user from the created users
            "date": datetime.utcnow(),
            "address": faker.address(),
            "status": random.choice(order_status)
        }
        new_order = Order(**order_data)
        db.session.add(new_order)
        orders.append(new_order)  # Store the created orders

    # Commit the orders to the database
    db.session.commit()

    # Fetch product IDs to use for order items
    product_ids = [product.id for product in Product.query.all()]

    # Create order items
    for order in orders:
        for _ in range(random.randint(1, 5)):  # Random number of items per order
            order_item = OrderItem(
                quantity=random.randint(1, 20),
                order_id=order.id,
                product_id=random.choice(product_ids)  # Use valid product IDs from the product list
            )
            db.session.add(order_item)

    # Commit all changes to the database
    db.session.commit()
