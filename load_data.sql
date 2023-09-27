-- load_data.sql

-- Carregar dados CSV1 em transactions_1
LOAD DATA INFILE '/var/lib/mysql-files/transactions_1.csv'
INTO TABLE transactions_1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;

-- Carregar dados CSV2 em transactions_2
LOAD DATA INFILE '/var/lib/mysql-files/transactions_2.csv'
INTO TABLE transactions_2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES;
