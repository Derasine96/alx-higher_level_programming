-- Creates the database hbtn_0d_2 and the user user_0d_2
-- Creates a database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creates a new user
CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Grants SELECT privileges
GRANT SELECT ON hbtn_0d_2.* TO 'user'@'localhost'
