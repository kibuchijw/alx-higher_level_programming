-- Creates the table 'unique_id' on MySQL server with a default unique value of 1 for 'id' 
CREATE TABLE IF NOT EXISTS `unique_id` (
	`id` INT DEFAULT 1 UNIQUE,
	`name` VARCHAR(256)
	);
