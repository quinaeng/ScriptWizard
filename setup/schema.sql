CREATE DATABASE scriptwizard;
USE scriptwizard;
CREATE TABLE scripts (
    id VARCHAR(255) PRIMARY KEY,
    type ENUM('python3', 'bash') NOT NULL,
    name TEXT,
    script TEXT,
    description TEXT
);
