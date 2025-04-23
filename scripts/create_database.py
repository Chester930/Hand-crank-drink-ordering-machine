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

# SQL 腳本內容
sql_script = """
-- 商品資料表
CREATE TABLE products (
    product_id INT IDENTITY(1,1) PRIMARY KEY, -- 自動遞增主鍵
    name NVARCHAR(100) NOT NULL,             -- 商品名稱
    price DECIMAL(10, 2) NOT NULL,           -- 商品價格
    description NVARCHAR(255),               -- 商品描述
    created_at DATETIME DEFAULT GETDATE(),   -- 建立時間
    updated_at DATETIME DEFAULT GETDATE()    -- 更新時間
);

-- 訂單資料表
CREATE TABLE orders (
    order_id INT IDENTITY(1,1) PRIMARY KEY,  -- 自動遞增主鍵
    user_id INT NOT NULL,                    -- 用戶 ID（假設外部系統管理用戶）
    order_date DATETIME DEFAULT GETDATE(),   -- 訂單日期
    total_amount DECIMAL(10, 2) NOT NULL,    -- 訂單總金額
    status NVARCHAR(50) DEFAULT 'Pending',   -- 訂單狀態（預設為 Pending）
    created_at DATETIME DEFAULT GETDATE(),   -- 建立時間
    updated_at DATETIME DEFAULT GETDATE()    -- 更新時間
);

-- 訂單商品中介資料表
CREATE TABLE order_items (
    order_item_id INT IDENTITY(1,1) PRIMARY KEY, -- 自動遞增主鍵
    order_id INT NOT NULL,                       -- 訂單編號（外鍵）
    product_id INT NOT NULL,                     -- 商品編號（外鍵）
    quantity INT NOT NULL,                       -- 商品數量
    price DECIMAL(10, 2) NOT NULL,               -- 單價（當前商品價格）
    created_at DATETIME DEFAULT GETDATE(),       -- 建立時間
    updated_at DATETIME DEFAULT GETDATE()        -- 更新時間
);

-- 交易資料表
CREATE TABLE transactions (
    transaction_id INT IDENTITY(1,1) PRIMARY KEY, -- 自動遞增主鍵
    order_id INT NOT NULL,                        -- 訂單編號（外鍵）
    payment_status NVARCHAR(50) NOT NULL,         -- 付款狀態（如 Paid, Failed）
    payment_date DATETIME DEFAULT GETDATE(),      -- 付款日期
    amount DECIMAL(10, 2) NOT NULL,               -- 交易金額
    created_at DATETIME DEFAULT GETDATE(),        -- 建立時間
    updated_at DATETIME DEFAULT GETDATE()         -- 更新時間
);

-- 外鍵約束
ALTER TABLE order_items
ADD CONSTRAINT FK_order_items_order FOREIGN KEY (order_id) REFERENCES orders(order_id);

ALTER TABLE order_items
ADD CONSTRAINT FK_order_items_product FOREIGN KEY (product_id) REFERENCES products(product_id);

ALTER TABLE transactions
ADD CONSTRAINT FK_transactions_order FOREIGN KEY (order_id) REFERENCES orders(order_id);
"""

# 建立資料庫連線並執行腳本
def execute_sql_script():
    try:
        # 建立連線
        connection = pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
        )
        cursor = connection.cursor()
        print("成功連接到資料庫！")

        # 執行 SQL 腳本
        for statement in sql_script.split(";"):
            if statement.strip():
                cursor.execute(statement)
                print(f"執行成功: {statement.strip()[:50]}...")

        # 提交變更
        connection.commit()
        print("資料表與外鍵約束已成功建立！")

    except Exception as e:
        print(f"執行過程中發生錯誤: {e}")
    finally:
        # 關閉連線
        cursor.close()
        connection.close()
        print("資料庫連線已關閉。")

# 執行腳本
if __name__ == "__main__":
    execute_sql_script()