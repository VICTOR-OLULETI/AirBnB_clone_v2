-- Create a new user hbnb_test (in localhost)
-- Create a database hbnb_test_db
-- password of hbnb_test_db set to hbnb_test_pwd
-- hbnb_test should have all privileges on database hbnb_test_db
-- hbnb_test should have select privileges on database performance_schema
-- if database hbnb_test_db or user hbnb_test exists, script should not fail.
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Creates database hbnb_test_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Grants all privileges on database on database hbnb_test_db to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grants select privileges on database performance schema to hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
