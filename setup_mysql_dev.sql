-- Create a new user hbnb_dev in localhost
-- password set to hbnb_dev_pwd
-- create database hbnb_dev_db
-- if hbnb_dev_db or user hbnb_dev exists, it should not fail
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Creates database hbnb_dev_db if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- Grants all priviledges on database hbnb_dev_db to hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Grants only select privilege on database performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
