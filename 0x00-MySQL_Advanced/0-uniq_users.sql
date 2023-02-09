-- Create a user table with the following fields:
-- id, email and name.
CREATE TABLE IF NOT EXISTS user (
    id int NOT NULL AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    PRIMARY KEY (id)
);