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
