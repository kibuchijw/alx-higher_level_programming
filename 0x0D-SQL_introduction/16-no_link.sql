-- Lists all records of 'second_table' except rows without a 'name' value, in descending order
SELECT `score`, `name` FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
