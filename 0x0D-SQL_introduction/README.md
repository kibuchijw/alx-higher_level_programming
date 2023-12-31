# 0x0D. SQL - Introduction

| Task | File |
| ---- | ---- |
| 0. List databases | [0-list_databases.sql](./0-list_databases.sql) |
| 1. Create a database | [1-create_database_if_missing.sql](./1-create_database_if_missing.sql) |
| 2. Delete a database | [2-remove_database.sql](./2-remove_database.sql) |
| 3. List tables | [3-list_tables.sql](./3-list_tables.sql) |
| 4. First table | [4-first_table.sql](./4-first_table.sql) |
| 5. Full description | [5-full_table.sql](./5-full_table.sql) |
| 6. List all in table | [6-list_values.sql](./6-list_values.sql) |
| 7. First add | [7-insert_value.sql](./7-insert_value.sql) |
| 8. Count 89 | [8-count_89.sql](./8-count_89.sql) |
| 9. Full creation | [9-full_creation.sql](./9-full_creation.sql) |
| 10. List by best | [10-top_score.sql](./10-top_score.sql) |
| 11. Select the best | [11-best_score.sql](./11-best_score.sql) |
| 12. Cheating is bad | [12-no_cheating.sql](./12-no_cheating.sql) |
| 13. Score too low | [13-change_class.sql](./13-change_class.sql) |
| 14. Average | [14-average.sql](./14-average.sql) |
| 15. Number by score | [15-groups.sql](./15-groups.sql) |
| 16. Say my name | [16-no_link.sql](./16-no_link.sql) |

Tasks
## 0. List databases
* A script that lists all databases of your MySQL server
## 1. Create a database
* A script that creates the database `hbtn_0c_0 in your MySQL server
	* If the database `hbtn_0c_0` already exists, the script should not fail
	* `SELECT` or `SHOW` statements are not allowed
## 2. Delete a database
* A script that deletes the database `hbtn_0c_0` in your MySQL server
	* If the database `hbtn_0c_0` doesn't exist, the script shouldn't fail
	* `SELECT` or `SHOW` statements are not allowed
## 3. List tables
* A script that lists all tables of a database in your MySQL server
	* Database name will be passed as argument of `mysql` command
## 4. First table
* A script that creates a table called `first_table` in the current database of a MySQL server
	* `first_table` description:
		* `id` INT
		* `name` VARCHAR(256)
	* Database name will be passed as argument of the `mysql` command
	* If `first_table` already exists, script should not fail
	* `SELECT` and `SHOW` statements are not allowed
## 5. Full description
* A script that prints the full description of a the table `first_table` from the database `hbtn_0c_0` in a MySQL server
	* Database name will be passed as argument of the `mysql` command
	* `DESCRIBE` or `EXPLAIN` statements are not allowed
## 6. List all in table
* A script that lists all rows of the table `first_table` from the database `hbtn_0c_0`
	* All fields should be printed
	* Database name will be passed as argument of the `mysql` command
* USAGE: `cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 7. First add
* A script that inserts a new row in the table `first_table`(database `hbtn_0c_0` in a MySQL server
		* New row:
			* `id` = `89`
			* `name` = `Best School`
		* The database name will be passed as argument of the `mysql` command
* USAGE: `cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 8. Count 89
* A script that displays the number of records with `id = 89` in `first_table` database `hbtn_0c_0`
	* The database name will be passed as argument of the `mysql` command
* USAGE: cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
## 9. Full creation
* A script that creates a table `second_table` in the `hbtn_0c_0` in a MySQL server and adds multiple rows
	* `second_table` description:
		* `id` INT
		* `name` VARCHAR(256)
		* `score` INT
	* Database name will be passed as argument to `mysql` command
	* If `second_table` already exists, script should not fail
	* `SELECT` and `SHOW` statements are not allowed
* USAGE: cat 9-full_creation.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
## 10. List by best
* A script that lists all records of `second_table` in `hbtn_0c_0`
	* Results should display both score and the name(in this order)
	* Records should be ordered by score(top first)
	* Database name will be passed as argument of `mysql` command
* USAGE: `cat 10-top_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 11. Select the best
* A script that lists all records with a `score >= 10` in `seond_table` of `hbtn_0c_0`
	* Results should display both score and the name(in this order)
	* Records should be ordered by score(top first)
	* Database name will be passed as argument of `mysql` command
* USAGE: `cat 11-best_score.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 12. Cheating is bad
* A script that updates the score of Bob to `10` in `second_table`
	* Bob's id value is not allowed, only the `name` field
	* Database name will be passed as argument of `mysql` command
* USAGE: `cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 13. Score too low
* A script that removes all records with `score <= 5` in `second_table` of `hbtn_0c_0`
	* Database name will be passed as argument of `mysql` command
## 14. Average
* A script that computes the score average of all records in `second_table` of `hbtn_0c_0`
	* Result column name should be `average`
	* Database name will be passed as argument of `mysql` command
* USAGE: `cat 14-average.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 15. Number by score
* A script that lists number of records with same score in `second_table` of `hbtn_0c_0`
	* Result should display:
		* The `score`
		* Number of records for this `score` with the label number
	* List should be sorted by number of records(descending)
	* Database name will be passed as argument of `mysql` command
* USAGE: `cat 15-groups.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
## 16. Say my name
* A script that lists all records of `second_table` in `hbtn_0c_0`
	* Rows without a `name` value shouldn't be listed
	* Results should display score and the name(in this order)
	* Records should be listed by descending order
	* Database name will be passed as argument of `mysql` command
* USAGE: `cat 16-no_link.sql | mysql -hlocalhost -uroot -p hbtn_0c_0`
