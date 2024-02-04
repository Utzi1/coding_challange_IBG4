-- create the databases
CREATE DATABASE IF NOT EXISTS database;
-- 
-- for authentification
ALTER USER 'root' IDENTIFIED WITH 'mysql_native_password' BY 'start123';
-- 
-- 
FLUSH PRIVILEGES;
