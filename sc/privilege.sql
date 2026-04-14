DROP USER IF EXISTS 'sample'@'localhost';
CREATE USER 'sample'@'localhost' IDENTIFIED BY '12345';
GRANT ALL ON student.* TO 'sample'@'localhost';
DROP USER IF EXISTS 'sample'@'%';
CREATE USER 'sample'@'%' IDENTIFIED BY '12345';
GRANT ALL ON student.* TO 'sample'@'%';
FLUSH PRIVILEGES;
