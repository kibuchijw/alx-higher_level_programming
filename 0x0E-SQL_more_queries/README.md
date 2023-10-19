# 0x0E. SQL - More queries

| Task | File |
| ---- | ---- |
| 0. My privileges! | [0-privileges.sql](./0-privileges.sql) |
| 1. Root user | [1-create_user.sql](./1-create_user.sql) |
| 2. Read user | [2-create_read_user.sql](./2-create_read_user.sql) |

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

