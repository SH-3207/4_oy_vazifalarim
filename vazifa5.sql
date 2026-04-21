
-- 1-masala


 select category,sum(quantity) total_sold from sales group by category;
+-------------+------------+
| category    | total_sold |
+-------------+------------+
| Electronics |         11 |
| Furniture   |          7 |
| Clothing    |         15 |
| Food        |         50 |
| Stationery  |         55 |
+-------------+------------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

-- 2 - masala;

select category , sum(price) as  jami_sotuv_summasi from sales group by category;
+-------------+--------------------+
| category    | jami_sotuv_summasi |
+-------------+--------------------+
| Electronics |               2450 |
| Furniture   |               2500 |
| Clothing    |                320 |
| Food        |                 17 |
| Stationery  |                 17 |
+-------------+--------------------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


-- 3 masala:

select category, avg(price)as ortacha_narx from sales group by category;
+-------------+--------------+
| category    | ortacha_narx |
+-------------+--------------+
| Electronics |     612.5000 |
| Furniture   |     625.0000 |
| Clothing    |      80.0000 |
| Food        |       4.2500 |
| Stationery  |       4.2500 |
+-------------+--------------+


-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

-- 4 - masala:

 select sale_date, sum(price * quantity )as jami_tushum from sales group by sale_date;
+------------+-------------+
| sale_date  | jami_tushum |
+------------+-------------+
| 2025-01-01 |        4030 |
| 2025-01-02 |        1605 |
| 2025-01-03 |        2278 |
| 2025-01-04 |        1348 |
+------------+-------------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

--  5 - masala:

select sum(price * quantity) as electronics_revenue from sales where category = "Electronics";
+---------------------+
| electronics_revenue |
+---------------------+
|                5050 |
+---------------------+

-- >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


 

-- 6 masala:

select category , sum(price * quantity) as sotuv_summasi from sales group by category having sum(price * quantity) > 2000 ;
+-------------+---------------+
| category    | sotuv_summasi |
+-------------+---------------+
| Electronics |          5050 |
| Furniture   |          2800 |
+-------------+---------------+

-- 7 masala;

 select category , avg(price) as price_100danoshiq from sales group by category having avg(price) > 100 ;
+-------------+-------------------+
| category    | price_100danoshiq |
+-------------+-------------------+
| Electronics |          612.5000 |
| Furniture   |          625.0000 |
+-------------+-------------------+

-- 8 masala:

 SELECT SUM(quantity) AS total_items
    -> FROM sales
    -> WHERE sale_date = '2025-01-01';
+-------------+
| total_items |
+-------------+
|          42 |
+-------------+

-- 9 masala:
SELECT category, SUM(quantity) AS total_quantity
    -> FROM sales
    -> GROUP BY category
    -> ORDER BY total_quantity DESC
    -> LIMIT 1;
+------------+----------------+
| category   | total_quantity |
+------------+----------------+
| Stationery |             55 |
+------------+----------------+

--  10 masala:

select category, sum(price * quantity) as jami_tushum from sales where quantity>3  group by category;
+-------------+-------------+
| category    | jami_tushum |
+-------------+-------------+
| Electronics |         750 |
| Furniture   |         400 |
| Clothing    |         600 |
| Food        |         165 |
| Stationery  |         196 |
+-------------+-------------+



















