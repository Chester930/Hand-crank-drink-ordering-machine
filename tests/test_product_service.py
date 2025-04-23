def test_create_product_with_category():
    category_id = create_category("Beverages", "Drinks and beverages")
    product_id = create_product("Milk Tea", "Delicious milk tea", 50.0, 100, category_id)
    product = get_product_by_id(product_id)
    assert product["category_id"] == category_id

def test_get_products_by_category():
    category_id = create_category("Snacks", "Light snacks and sides")
    create_product("Chips", "Crispy chips", 30.0, 200, category_id)
    products = get_products_by_category(category_id)
    assert len(products) > 0
    assert products[0]["name"] == "Chips"