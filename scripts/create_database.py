import pyodbc
from dotenv import load_dotenv
import os

# 載入 .env 檔案
load_dotenv()

# 資料庫連線設定
server = os.getenv("DB_SERVER")  # 從 .env 檔案讀取
database = os.getenv("DB_DATABASE")
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

# 建立資料表的 SQL 腳本
create_tables_script = """
-- 用戶資料表
IF OBJECT_ID('users', 'U') IS NULL
CREATE TABLE users (
    user_id INT IDENTITY(1,1) PRIMARY KEY,
    username NVARCHAR(50) NOT NULL UNIQUE,
    password NVARCHAR(255) NOT NULL,
    email NVARCHAR(100) NOT NULL UNIQUE,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

-- 商品分類表
IF OBJECT_ID('categories', 'U') IS NULL
CREATE TABLE categories (
    category_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(50) NOT NULL UNIQUE,
    description NVARCHAR(255),
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE()
);

-- 商品資料表
IF OBJECT_ID('products', 'U') IS NULL
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    description NVARCHAR(255),
    stock INT NOT NULL DEFAULT 0,
    category_id INT,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);

-- 訂單資料表
IF OBJECT_ID('orders', 'U') IS NULL
CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,
    user_id INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    status NVARCHAR(20) DEFAULT 'pending',
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- 訂單項目資料表
IF OBJECT_ID('order_items', 'U') IS NULL
CREATE TABLE order_items (
    order_item_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- 付款資料表
IF OBJECT_ID('payments', 'U') IS NULL
CREATE TABLE payments (
    payment_id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT NOT NULL,
    payment_method NVARCHAR(50) NOT NULL,
    status NVARCHAR(20) DEFAULT 'unpaid',
    transaction_id NVARCHAR(100),
    created_at DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);
"""

# 執行 SQL 腳本的函式
def execute_sql_script(script, connection):
    cursor = connection.cursor()
    try:
        for statement in script.split(";"):
            if statement.strip():
                try:
                    cursor.execute(statement)
                    print(f"執行成功: {statement.strip()[:50]}...")
                except Exception as e:
                    print(f"執行失敗: {statement.strip()[:50]}...")
                    print(f"錯誤訊息: {e}")
                    print(f"完整 SQL: {statement.strip()}")
        connection.commit()
    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")
    finally:
        cursor.close()

# 主程式
def main():
    try:
        # 建立資料庫連線
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        )
        print("成功連接到資料庫！")

        # 建立新的資料表
        print("正在建立新的資料表...")
        execute_sql_script(create_tables_script, connection)

        print("資料表已成功建立！")

    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
            print("資料庫連線已關閉。")

# 執行主程式
if __name__ == "__main__":
    main()