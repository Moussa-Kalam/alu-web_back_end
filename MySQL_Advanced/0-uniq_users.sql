-- Create a table users with unique values
CREATE TABLE IF NOT EXISTS users (
    id int AUTOINCREMENT NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id)
);