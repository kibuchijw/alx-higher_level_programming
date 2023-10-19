# 0x0E. SQL - More queries

| Task | File |
| ---- | ---- |
| 0. My privileges! | [0-privileges.sql](./0-privileges.sql) |
| 1. Root user | [1-create_user.sql](./1-create_user.sql) |
| 2. Read user | [2-create_read_user.sql](./2-create_read_user.sql) |
| 3. Always a name | [3-force_name.sql](./3-force_name.sql) |
| 4. ID can't be null | [4-never_empty.sql](./4-never_empty.sql) |
| 5. Unique ID | [5-unique_id.sql](./5-unique_id.sql) |

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
* Script that create table `unique_id` on MySQL server
	* `unique_id` description:
		* `id` INT with default value `1` and must be unique
		* `name` VARCHAR(256)
	* Database name passed as an argument of `mysql` command
	* If the table `unique_id` already exists, script should not fail
	
