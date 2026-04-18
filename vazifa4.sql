create database noutbooklar;

 use noutbooklar;

 create table kompyuter(brand varchar(50), model varchar(50), cpu varchar(50), frequency real, ram int , os varchar(50), price int );

 insert into kompyuter values('Apple', 'MacBook Pro 14', 'M2 Pro', 3.5, 16, 'macOS', 2400),    ('Apple', 'MacBook Air', 'M1', 3.2, 8, 'macOS', 950),    ('Apple', 'MacBook Pro 16', 'M3 Max', 4.0, 32, 'macOS', 3000);

 insert into kompyuter values('ASUS', 'ZenBook 14', 'Intel Core i7', 2.8, 16, 'Windows 11', 1200),    ('ASUS', 'VivoBook S15', 'Intel Core i5', 2.4, 8, 'Windows 10', 750),    ('ASUS', 'TUF Gaming', 'Intel Core i5', 4.5, 8, 'Windows 11', 900),    ('ASUS', 'ROG Zephyrus', 'AMD Ryzen 9', 4.9, 16, 'Windows 11', 2100);

 insert into kompyuter values('HP', 'Pavilion 15', 'Intel Core i5', 2.4, 8, 'Windows 10', 650),    ('HP', 'Spectre x360', 'Intel Core i7', 2.8, 16, 'Windows 11', 1350),    ('HP', 'Victus', 'AMD Ryzen 5', 3.9, 8, 'FreeDOS', 800);

insert into kompyuter values('Dell', 'XPS 13', 'Intel Core i7', 3.0, 16, 'Windows 11', 1500),    ('Dell', 'Inspiron 15', 'Intel Core i3', 2.1, 4, 'Windows 10', 450),    ('Dell', 'Latitude', 'Intel Core i5', 2.6, 8, 'Ubuntu 20.04', 850);

insert into kompyuter values('Lenovo', 'ThinkPad X1', 'Intel Core i7', 2.8, 16, 'Windows 11', 1700),    ('Lenovo', 'IdeaPad 3', 'AMD Ryzen 3', 2.6, 4, 'Windows 10', 420),    ('Lenovo', 'Legion 5', 'AMD Ryzen 7', 4.2, 16, 'FreeDOS', 1100);

insert into kompyuter values('Acer', 'Swift 3', 'Intel Core i5', 2.4, 8, 'Windows 10', 600),    ('Acer', 'Aspire 5', 'Intel Core i5', 2.4, 8, 'Windows 11', 550),    ('Acer', 'Nitro 5', 'Intel Core i7', 4.4, 16, 'Windows 11', 1050),    ('MSI', 'Modern 14', 'Intel Core i3', 2.1, 8, 'Windows 10', 480);

 select * from kompyuter;
+--------+----------------+---------------+-----------+------+--------------+-------+
| brand  | model          | cpu           | frequency | ram  | os           | price |
+--------+----------------+---------------+-----------+------+--------------+-------+
| Apple  | MacBook Pro 14 | M2 Pro        |       3.5 |   16 | macOS        |  2400 |
| Apple  | MacBook Air    | M1            |       3.2 |    8 | macOS        |   950 |
| Apple  | MacBook Pro 16 | M3 Max        |         4 |   32 | macOS        |  3000 |
| ASUS   | ZenBook 14     | Intel Core i7 |       2.8 |   16 | Windows 11   |  1200 |
| ASUS   | VivoBook S15   | Intel Core i5 |       2.4 |    8 | Windows 10   |   750 |
| ASUS   | TUF Gaming     | Intel Core i5 |       4.5 |    8 | Windows 11   |   900 |
| ASUS   | ROG Zephyrus   | AMD Ryzen 9   |       4.9 |   16 | Windows 11   |  2100 |
| HP     | Pavilion 15    | Intel Core i5 |       2.4 |    8 | Windows 10   |   650 |
| HP     | Spectre x360   | Intel Core i7 |       2.8 |   16 | Windows 11   |  1350 |
| HP     | Victus         | AMD Ryzen 5   |       3.9 |    8 | FreeDOS      |   800 |
| Dell   | XPS 13         | Intel Core i7 |         3 |   16 | Windows 11   |  1500 |
| Dell   | Inspiron 15    | Intel Core i3 |       2.1 |    4 | Windows 10   |   450 |
| Dell   | Latitude       | Intel Core i5 |       2.6 |    8 | Ubuntu 20.04 |   850 |
| Lenovo | ThinkPad X1    | Intel Core i7 |       2.8 |   16 | Windows 11   |  1700 |
| Lenovo | IdeaPad 3      | AMD Ryzen 3   |       2.6 |    4 | Windows 10   |   420 |
| Lenovo | Legion 5       | AMD Ryzen 7   |       4.2 |   16 | FreeDOS      |  1100 |
| Acer   | Swift 3        | Intel Core i5 |       2.4 |    8 | Windows 10   |   600 |
| Acer   | Aspire 5       | Intel Core i5 |       2.4 |    8 | Windows 11   |   550 |
| Acer   | Nitro 5        | Intel Core i7 |       4.4 |   16 | Windows 11   |  1050 |
| MSI    | Modern 14      | Intel Core i3 |       2.1 |    8 | Windows 10   |   480 |
+--------+----------------+---------------+-----------+------+--------------+-------+
20 rows in set (0.00 sec)

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


-- 1 masala: 

select * from kompyuter order by price desc limit 1;
+-------+----------------+--------+-----------+------+-------+-------+
| brand | model          | cpu    | frequency | ram  | os    | price |
+-------+----------------+--------+-----------+------+-------+-------+
| Apple | MacBook Pro 16 | M3 Max |         4 |   32 | macOS |  3000 |
+-------+----------------+--------+-----------+------+-------+-------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


--  2 masala:

select * from kompyuter order by price asc limit 1;
+--------+-----------+-------------+-----------+------+------------+-------+
| brand  | model     | cpu         | frequency | ram  | os         | price |
+--------+-----------+-------------+-----------+------+------------+-------+
| Lenovo | IdeaPad 3 | AMD Ryzen 3 |       2.6 |    4 | Windows 10 |   420 |
+--------+-----------+-------------+-----------+------+------------+-------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


-- 3 masala:

 select frequency from kompyuter where price between 400 and 1000  and cpu like "%intel%";
+-----------+
| frequency |
+-----------+
|       2.4 |
|       4.5 |
|       2.4 |
|       2.1 |
|       2.6 |
|       2.4 |
|       2.4 |
|       2.1 |
+-----------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


-- 4 masala;

 select count(*) from kompyuter where brand ="apple";
+----------+
| count(*) |
+----------+
|        3 |
+----------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 


--  5 masala :

select * from kompyuter where os like "%windows%" and ram=8 and brand= "asus" order by price asc ;
+-------+--------------+---------------+-----------+------+------------+-------+
| brand | model        | cpu           | frequency | ram  | os         | price |
+-------+--------------+---------------+-----------+------+------------+-------+
| ASUS  | VivoBook S15 | Intel Core i5 |       2.4 |    8 | Windows 10 |   750 |
| ASUS  | TUF Gaming   | Intel Core i5 |       4.5 |    8 | Windows 11 |   900 |
+-------+--------------+---------------+-----------+------+------------+-------+



