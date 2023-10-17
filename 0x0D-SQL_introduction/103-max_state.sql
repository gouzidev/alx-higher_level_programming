-- btyh
SELECT * FROM (SELECT  state, MAX(value) AS max_temp FROM hbtn_0c_0.temperatures AS tb1 GROUP BY state) AS tb2 ORDER BY state limit 3;

