-- Lists all records of the table second_table.
-- Records are ordered by score
SELECT `score`, `name`
FROM `second_table`
WHERE `score` >= 10
ORDER BY `score` DESC;
