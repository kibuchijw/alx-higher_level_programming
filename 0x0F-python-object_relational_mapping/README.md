# 0x0F. Python - Object-relational mapping

## Learning Objectives

### General

* How to connect to a MySQL database from a Python script
* How to `SELECT` rows in a MySQL table from a Python script
* How to `INSERT` rows in a MySQL table from a Python script
* What ORM means
* How to map a Python Class to a MySQL table
* How to create a Python Virtual Environment

| Task | File |
| ---- | ---- |
| 0. Get all states | [0-select_states.py](./0-select_states.py) |
| 1. Filter states | [1-filter_states.py](./1-filter_states.py) |
| 2. Filter states by user input | [2-my_filter_states.py](./2-my_filter_states.py) |
| 3. SQL Injection... | [3-my_safe_filter_states.py](./3-my_safe_filter_states.py) |
| 4. Cities by states | [4-cities_by_state.py](./4-cities_by_state.py) |
| 5. All cities by state | [5-filter_cities.py](./5-filter_cities.py) |
| 6. First state model | [model_state.py](./model_state.py) |
| 7. All states via SQLAlchemy | [7-model_state_fetch_all.py](./7-model_state_fetch_all.py) |
| 8. First state | [8-model_state_fetch_first.py](./8-model_state_fetch_first.py) |

## Tasks
### 0. Get all states
* A script that lists all `states` from the database `hbtn_0e_0_usa`:
	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
	* You must use the module `MySQLdb` (`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* Resulsts must be shown exactly as per example
	* Your code should not be executed when imported
### 1. Filter states
* A script that lists all `states` with a `name` starting with `N`(Upper N) from the database `hbtn_0e_0_usa`:
	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
	* You must use the module `MySQLdb`(`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* Results must be displayed as they are in the example given
	* Your code should not be executed when imported
### 2. Filter states by user input
* A script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.	
	* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
	* You must use the module `MySQLdb`(`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* Results must be displayed as they are in the example given
	* Your code should not be executed when imported
### 3. SQL Injection...
* A script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. But this time, write one that is safe from MySQL injections!
	* Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name searched` (no argument validation needed)
	* You must use the module `MySQLdb`(`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* Results must be displayed as they are in the example given
	* Your code should not be executed when imported
### 4. Cities by states
* A script that lists all `cities` from the database `hbtn_0e_4_usa`
	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `MySQLdb`(`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `cities.id`
	* You can only use `execute()` once
	* Results must be displayed as they are in the example given
	* Your code should not be executed when imported
### 5. All cities by state
* A script taht takes in the name of a state as an argument and lists all `cities` of that state, using the database `hbtn_0e_4_usa`
	* Your script should take 3 arguments: `mysql username`, `mysql password`, `database name` and `state name` (SQL injection free!)
	* You must use the module `MySQLdb`(`import MySQLdb`)
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `cities.id`
	* You can only use `execute()` once
	* Results must be displayed as they are in the example given
	* Your code should not be executed when imported
### 6. First state model
* A python file that contains the class definition of a `State` and an instance `Base = declarative_base()`:
	* `State` class:
		* inherits from `Base`[Tips](https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/basic_use.html)
		* links to the MySQL table `states`
		* class attribute `id` that represents a column of an auto-generated, unique integer, can't be null and is a primary key
		* class attribute `name` that represents a column of a string with maximum 128 characters and can't be null
	* You must use the module `SQLAlchemy`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* **WARNING**: all classes who inherit from `Base` **must** be imported before calling `Base.metadata.create_all(engine)`
### 7. All states via SQLAlchemy
* A script that lists all `State` objects from the database `hbtn_0e_6_usa`
	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state`-`from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* Results must be sorted in ascending order by `states.id`
	* The results must be displayed as they are in the example given
	* Your code should not be executed when imported
### 8. First state
* A script that prints the first `State` object from the database `hbtn_0e_6_usa`
	* Your script should take 3 arguments: `mysql username`, `mysql password` and `database name`
	* You must use the module `SQLAlchemy`
	* You must import `State` and `Base` from `model_state`-`from model_state import Base, State`
	* Your script should connect to a MySQL server running on `localhost` at port `3306`
	* The state you display must be the first in `states.id`
	* You are not allowed to fetch all states from the database before displaying the result
	* The results must be displayed as they are in the example given
	* If the table `states` is empty, print `Nothing` followed by a new line
	* Your code should not be executed when imported
