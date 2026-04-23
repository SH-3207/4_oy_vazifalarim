-- 1 Masala:

 SELECT a.name, JSON_ARRAYAGG(j.name) AS janrlar
    -> FROM book AS b
    -> INNER JOIN janr AS j ON b.j_id = j.id
    -> INNER JOIN author AS a ON b.a_id = a.id
    -> WHERE a.name = 'Alisher Navoiy'
    -> GROUP BY a.name;
+----------------+-----------------------------------+
| name           | janrlar                           |
+----------------+-----------------------------------+
| Alisher Navoiy | ["komediya", "DRAMMA", "TARIXIY"] |
+----------------+-----------------------------------+

-- _________________________________________________________________

--  2 Masala:

select a.name, JSON_ARRAYAGG(j.name) as janrlar
    -> from book as b
    -> inner join janr as j on b.j_id = j.id
    -> inner join author as a on b.a_id = a.id
    -> Group by a.name;
+----------------+-----------------------------------+
| name           | janrlar                           |
+----------------+-----------------------------------+
| Agata K        | ["DRAMMA", "komediya"]            |
| Alisher Navoiy | ["DRAMMA", "komediya", "TARIXIY"] |
| Sheksper       | ["DRAMMA", "DRAMMA", "TARIXIY"]   |
| Tolstoy        | ["TARIXIY", "ERTAK"]              |
+----------------+-----------------------------------+

-- _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

-- 3 Masala;

 select a.name as Muallif, count(*) as "Nechta kitob yozgani"
    -> from book as b
    -> inner join janr as j on b.j_id = j.id inner join author as a on b.a_id = a.id group by a.name;
+----------------+----------------------+
| Muallif        | Nechta kitob yozgani |
+----------------+----------------------+
| Sheksper       |                    3 |
| Alisher Navoiy |                    3 |
| Agata K        |                    2 |
| Tolstoy        |                    2 |
+----------------+----------------------+

-- ________________________________________________________________________________________________________

--  4 Masala:

 SELECT j.name AS 'Eng ko\'p yozilgan janr', COUNT(*) AS 'Kitoblar soni'
    -> FROM book AS b
    -> INNER JOIN janr AS j ON b.j_id = j.id
    -> GROUP BY j.name
    -> ORDER BY COUNT(*) DESC
    -> LIMIT 1;
+------------------------+---------------+
| Eng ko'p yozilgan janr | Kitoblar soni |
+------------------------+---------------+
| DRAMMA                 |             4 |
+------------------------+---------------+

-- ________________________________________________________________________________________

--  5 Masala:

SELECT a.name AS 'Muallif', j.name AS 'Asosiy janri', COUNT(*) AS 'Kitoblar soni'
    -> FROM book AS b
    -> INNER JOIN author AS a ON b.a_id = a.id
    -> INNER JOIN janr AS j ON b.j_id = j.id
    -> GROUP BY a.name, j.name
    -> ORDER BY a.name, COUNT(*) DESC;
+----------------+--------------+---------------+
| Muallif        | Asosiy janri | Kitoblar soni |
+----------------+--------------+---------------+
| Agata K        | komediya     |             1 |
| Agata K        | DRAMMA       |             1 |
| Alisher Navoiy | komediya     |             1 |
| Alisher Navoiy | DRAMMA       |             1 |
| Alisher Navoiy | TARIXIY      |             1 |
| Sheksper       | DRAMMA       |             2 |
| Sheksper       | TARIXIY      |             1 |
| Tolstoy        | ERTAK        |             1 |
| Tolstoy        | TARIXIY      |             1 |
+----------------+--------------+---------------+

-- ______________________________________________________________________________________________

-- 6 Masala;

 SELECT a.name AS 'Muallif', b.name AS 'Kitob nomi', SUM(b.amount) AS 'Jami sotilgan'
    -> FROM book AS b
    -> INNER JOIN author AS a ON b.a_id = a.id
    -> GROUP BY a.name, b.name
    -> ORDER BY SUM(b.amount) DESC
    -> LIMIT 1;
+---------+-------------+---------------+
| Muallif | Kitob nomi  | Jami sotilgan |
+---------+-------------+---------------+
| Tolstoy | Oq kechalar |           205 |
+---------+-------------+---------------+