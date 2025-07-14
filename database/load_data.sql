LOAD DATA INFILE '/var/lib/mysql-files/raw_transactions.csv'
INTO TABLE transactions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(transaction_id, customer_id, transaction_time, amount, merchant, category, is_fraud);

-- tip: Tip: You may have to adjust secure-file-priv for MySQL.
