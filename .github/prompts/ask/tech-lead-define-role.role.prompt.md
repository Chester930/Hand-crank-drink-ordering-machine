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