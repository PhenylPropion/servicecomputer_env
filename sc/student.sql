# -*- coding: utf-8 -*- */

########################################################################
# studentデータベース

CREATE DATABASE IF NOT EXISTS student;
USE student;

########################################################################
# studentsテーブル

#DROP TABLE IF EXISTS students;
CREATE TABLE IF NOT EXISTS students (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  studentID varchar(7),
  name varchar(32)
) ENGINE=InnoDB, CHARSET=utf8;

########################################################################
# 初期化

TRUNCATE TABLE students;
INSERT INTO students(studentID,name)
VALUES ('99K1191','法政 太郎'),
       ('99K1192','法政 次郎'),
       ('99K1193','法政 三郎'),
       ('99K1194','小金井 花子'),
       ('99K1195','市ヶ谷 桜'),
       ('99K1198','架空 学');

DROP USER IF EXISTS 'sample'@'localhost';
CREATE USER 'sample'@'localhost' IDENTIFIED BY '12345';
GRANT ALL ON student.* TO 'sample'@'localhost';
FLUSH PRIVILEGES;
