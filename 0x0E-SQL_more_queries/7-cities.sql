-- Creates database 'hbtn_0d_usa' and table 'cities' in the database
-- 'id' is unique, auto generates and can't be null and is a primary key
-- 'state_id' can't be null and must be a 'FOREIGN KEY' that refs to 'id' of 'states'
-- VARCHAR can't be null
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (
	PRIMARY KEY (`id`),
	`id` INT NOT NULL AUTO_INCREMENT,
	`state_id` INT NOT NULL,
	`name` VARCHAR(256) NOT NULL,
	FOREIGN KEY (`state_id`)
	REFERENCES `hbtn_0d_usa`.`states`(`id`)
	);
