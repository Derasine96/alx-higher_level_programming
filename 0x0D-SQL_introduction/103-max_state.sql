-- Displays the max temperature of each state, ordered by state name.
SELECT MAX(statde)
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
