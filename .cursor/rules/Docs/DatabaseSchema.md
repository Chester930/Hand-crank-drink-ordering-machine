# Database Schema: 手搖飲料點餐機

## 版本：2025年4月23日 - 初始草案

## 1. 用戶表 (Users)

* **欄位**：

  * `id` (主鍵，自增整數)
  * `username` (唯一，字串，長度 50)
  * `password` (字串，長度 255)
  * `email` (唯一，字串，長度 100)
  * `role` (字串，長度 20，預設為 'customer')
  * `is_active` (布林值，預設為 true)
  * `created_at` (時間戳記，預設為當前時間)
  * `updated_at` (時間戳記，預設為當前時間)

## 2. 產品表 (Products)

* **欄位**：

  * `id` (主鍵，自增整數)
  * `name` (字串，長度 100)
  * `description` (文字，可為空)
  * `price` (浮點數，非負)
  * `stock` (整數，非負)
  * `category_id` (外鍵，參考 Categories.id)
  * `image_url` (字串，長度 255，可為空)
  * `created_at` (時間戳記，預設為當前時間)
  * `updated_at` (時間戳記，預設為當前時間)

## 3. 商品分類表 (Categories)

* **欄位**：

  * `category_id` (主鍵，自增整數)
  * `name` (字串，長度 50，唯一)
  * `description` (文字，可為空)
  * `created_at` (時間戳記，預設為當前時間)
  * `updated_at` (時間戳記，預設為當前時間)

## 4. 訂單表 (Orders)

* **欄位**：

  * `id` (主鍵，自增整數)
  * `user_id` (外鍵，參考 Users.id)
  * `total_price` (浮點數，非負)
  * `status` (字串，長度 20，預設為 'pending')
  * `order_date` (時間戳記，預設為當前時間)
  * `delivery_address` (文字，可為空)
  * `created_at` (時間戳記，預設為當前時間)
  * `updated_at` (時間戳記，預設為當前時間)

## 5. 訂單項目表 (Order_Items)

* **欄位**：

  * `id` (主鍵，自增整數)
  * `order_id` (外鍵，參考 Orders.id)
  * `product_id` (外鍵，參考 Products.id)
  * `quantity` (整數，非負)
  * `price` (浮點數，非負)

## 6. 付款表 (Payments)

* **欄位**：

  * `id` (主鍵，自增整數)
  * `order_id` (外鍵，參考 Orders.id)
  * `payment_method` (字串，長度 50)
  * `status` (字串，長度 20，預設為 'unpaid')
  * `transaction_id` (字串，長度 100，可為空)
  * `amount` (浮點數，非負)
  * `payment_date` (時間戳記，預設為當前時間)
  * `created_at` (時間戳記，預設為當前時間)

## 7. 系統操作日誌表 (Audit_Logs)

* **欄位**：

  * `id` (主鍵，自增整數)
  * `action` (字串，長度 100)
  * `user_id` (外鍵，參考 Users.id)
  * `timestamp` (時間戳記，預設為當前時間)
  * `details` (文字，可為空)

## 關聯性

* Users 與 Orders：一對多
* Orders 與 Order_Items：一對多
* Products 與 Order_Items：多對多
* Orders 與 Payments：一對一
* Products 與 Categories：多對一