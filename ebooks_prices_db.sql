-- Utwórz bazę danych
CREATE DATABASE IF NOT EXISTS ebook_price_exchange;

-- Użyj nowo utworzonej bazy danych
\c ebook_price_exchange

-- Utwórz tabelę ebook_prices
CREATE TABLE IF NOT EXISTS ebook_prices (
    id SERIAL PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    title VARCHAR(100) NOT NULL,
    original_price DECIMAL(10, 2) NOT NULL,
    date DATE NOT NULL,
    exchange_rate DECIMAL(10, 4) NOT NULL,
    price_pln DECIMAL(10, 2) NOT NULL,
    table_no VARCHAR(20) NOT NULL
);
