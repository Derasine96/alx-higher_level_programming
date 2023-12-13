-- creates the table and database on your MySQL server.
-- create database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa
-- Create a table
CREATE TABLE IF NOT EXISTS `states` (
	`id` INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
	`name` VARCHAR(256) NOT NULL
);
