def seed_categories():
    categories = [
        {"name": "Beverages", "description": "Drinks and beverages"},
        {"name": "Snacks", "description": "Light snacks and sides"}
    ]
    for category in categories:
        db.execute("INSERT INTO categories (name, description) VALUES (?, ?)", (category["name"], category["description"]))

def seed_products():
    products = [
        {"name": "Milk Tea", "price": 50.0, "stock": 100, "category_id": 1},
        {"name": "Green Tea", "price": 40.0, "stock": 150, "category_id": 1},
        {"name": "Chips", "price": 30.0, "stock": 200, "category_id": 2}
    ]
    for product in products:
        db.execute("INSERT INTO products (name, price, stock, category_id) VALUES (?, ?, ?, ?)",
                   (product["name"], product["price"], product["stock"], product["category_id"]))