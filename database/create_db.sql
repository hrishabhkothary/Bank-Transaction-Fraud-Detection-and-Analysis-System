CREATE DATABASE IF NOT EXISTS bank_transactions;

USE bank_transactions;

CREATE TABLE IF NOT EXISTS transactions (
    transaction_id VARCHAR(255) PRIMARY KEY,
    customer_id INT,
    transaction_time DATETIME,
    amount DECIMAL(10,2),
    merchant VARCHAR(255),
    category VARCHAR(50),
    is_fraud TINYINT(1)
);
