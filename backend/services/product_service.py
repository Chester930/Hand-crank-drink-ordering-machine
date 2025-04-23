def create_product(name, description, price, stock, category_id, image_url=None):
    query = """
    INSERT INTO products (name, description, price, stock, category_id, image_url, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, GETDATE(), GETDATE())
    """
    db.execute(query, (name, description, price, stock, category_id, image_url))

def get_products_by_category(category_id):
    query = "SELECT * FROM products WHERE category_id = ?"
    return db.fetch_all(query, (category_id,))