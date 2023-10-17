-- btyh
SELECT * FROM (SELECT  city, AVG(value) AS avg_temp FROM hbtn_0c_0.temperatures AS tb1 WHERE month < 9 AND month > 6 GROUP BY city) AS tb2 ORDER BY avg_temp DESC limit 3;

