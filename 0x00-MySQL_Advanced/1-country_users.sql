-- Create a table `users` with the following attributes.
-- id, email, name, country where country is a choice between 3.
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US',
    PRIMARY KEY (id)
);