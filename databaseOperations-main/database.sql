CREATE DATABASE operations_db;

\c operations_db;

CREATE TABLE IF NOT EXISTS user_details (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);