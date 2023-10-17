-- hh
SELECT * FROM (SELECT city, AVG(value) AS avg_temp FROM temperatures as tb1 GROUP BY city)
 as tb2 ORDER BY avg_temp DESC;

