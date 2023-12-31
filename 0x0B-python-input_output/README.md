## Python - Input/Output
* A comprehensive dive into the python file operations
### Read file
* A function that reads a text file (`UTF8`) and prints it to stdout
### Write to a file
* Function that writes a string to a text file (`UTF8`) and returns number of characters written
### To JSON string
* Function that returns JSON representation of an object(string)
### From JSON string to Object
* Function that returns an object(Python data structure) represented by a JSON string
### Save Object to a file
* Function that writes an Object to a text file, using a JSON representation
### Create Object from a JSON file
* Function that creates an Object from a JSON file
### Load, add, save
* Script that adds all arguments to a Python list, and then save them to a file
### Class to JSON
* Function that returns the dictionary description with simple data structure(list, dictionary, string, integer and boolean) for JSON serialization of an object
### Student to JSON
* A class `Student` that defines a student by:
	* Public instance attributes:
		* `first_name`
		* `last_name`
		* `age`
### Student to JSON with filter
* A class `Student` that defines a student by:(based on `9-student.py`)
	* id `attrs` is a list of strings, only attribute names contained in the list must be retrieved
	* Otherwise, all attributes must be retrieved
### Student to disk and reload
* A class `Student` that defines a student by:(based on `10-student.py`)
	* Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance
### Pascal's Triangle
* Function `def pascal_triangle(n):` that returns a list of lists of integers representing the Pascal's triangle of `n`
### Search and update
* Function that inserts a line of text to a file, after each line containing a specific string
