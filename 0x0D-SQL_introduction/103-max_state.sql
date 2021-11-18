-- Write a script that displays the max temperature of eachate (ordered by State name).
SELECT state, Max(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC LIMIT 3;
