# 0x0E. SQL - More queries

| Task | File |
| ---- | ---- |
| 0. My privileges! | [0-privileges.sql](./0-privileges.sql) |
| 1. Root user | [1-create_user.sql](./1-create_user.sql) |
| 2. Read user | [2-create_read_user.sql](./2-create_read_user.sql) |
| 3. Always a name | [3-force_name.sql](./3-force_name.sql) |
| 4. ID can't be null | [4-never_empty.sql](./4-never_empty.sql) |
| 5. Unique ID | [5-unique_id.sql](./5-unique_id.sql) |
| 6. States table | [6-states.sql](./6-states.sql) |
| 7. Cities table | [7-cities.sql](./7-cities.sql) |
| 8. Cities of California | [8-cities_of_california_subquery.sql](./8-cities_of_california_subquery.sql) |
| 9. Cities by States | [9-cities_by_state_join.sql](./9-cities_by_state_join.sql) |

# Tasks
## 0. My privileges!
* Script that lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on the server(in `localhost`)
## 1. Root user
* Script that creates the MySQL server user `user_0d_1`
	* `user_0d_1` should have all privileges
	* `user_0d_1` password should be set to `user_0d_1_pwd`
	* If `user_0d_1` already exists, script should not fail
## 2. Read user
* Script that creates the database `hbtn_0d_2` and the user `user_0d_2`
	* `user_0d_2` should have only SELECT privilege in the database `hbtn_0d_2`
	* `user_0d_2` password should be set to `user_0d_2_pwd`
	* if database `hbtn_0d_2` already exists, script should not fail
## 3. Always a name
* Script that creates the table `force_name` on MySQL server
	* `force_name` description:
		* `id` INT
		* `name` VARCHAR(256) can't be null
	* Database name passed as an argument of `mysql` command
	* If `force_name` already exists, script should not fail
## 4. ID can't be null
* Script that creates table `id_not_null` on MySQL server
	* `id_not_null` description:
		* `id` INT with the default value `1`
		* `name` VARCHAR(256)
	* Database name passed as an argument of `mysql` command
	* If the table `id_not_null` already exists, script should not fail
## 5. Unique ID
* Script that creates table `unique_id` on MySQL server
	* `unique_id` description:
		* `id` INT with default value `1` and must be unique
		* `name` VARCHAR(256)
	* Database name passed as an argument of `mysql` command
	* If the table `unique_id` already exists, script should not fail
## 6. States table
* Script that creates database `hbtn_0d_usa` and the table `states`(in the database hbtn_0d_usa`) on MySQL server
	* `states` description:
		* `id` INT unique, auto generated, can't be null and is a primary key
		* `name` VARCHAR(256) can't be null
	* If the database `hbtn_0d_usa` already exists, script should not fail
	* If the table `states` already exists, script should not fail
## 7. Cities table
* Script that creates databade `hbtn_0d_usa` and table `cities`(int the database `hbtn_0d_usa`) on MySQL server
	* `cities` description:
		* `id` INT unique, auto generated, can't be null and is a primary key
		* `state_id` INT, can't be null and must be a `FOREIGN KEY` that references to `id` of the `states` table
		* `name` VARCHAR(256) can't be null
	* If the database `hbtn_0d_usa` already, exists, script should not fail
	* If the table `cities` already exists, script should not fail
## 8. Cities of California
* Script that lists all cities of California that can be foung in the database `hbtn_0d_usa`
	* `states` table contains only one record where `name`=`California`(but the `id` can be different)
	* Results must be sorted in ascending order by `cities.id`
	* `JOIN` keyword is not allowed
	* Database name will be passed as argument of the `mysql` command
## 9. Cities by States
* Script that lists all cities contained in the database `hbtn_0d_usa`
	* Each record should display: `cities.id`-`cities.name`-`states.name`
	* Results must be sorted in ascending order by `cities.id`
	* Only one `SELECT` statement is allowed
	* Database name will be passed as argument of the `mysql` command
	
