-- Criação da tabela para o primeiro CSV (transactions_1), se ela não existir
CREATE TABLE IF NOT EXISTS transactions_1 (
    time VARCHAR(10) NOT NULL,
    status VARCHAR(255) NOT NULL,
    f0_ INT NOT NULL
);

-- Criação da tabela para o segundo CSV (transactions_2), se ela não existir
CREATE TABLE IF NOT EXISTS transactions_2 (
    time VARCHAR(10) NOT NULL,
    status VARCHAR(255) NOT NULL,
    f0_ INT NOT NULL
);
