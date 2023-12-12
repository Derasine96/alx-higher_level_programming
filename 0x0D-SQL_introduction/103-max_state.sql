-- Displays the max temperature of each state, ordered by state name.
SELECT MAX(state)
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
