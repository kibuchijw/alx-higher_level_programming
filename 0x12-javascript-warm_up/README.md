# 0x12. JavaScript - Warm up

## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between `var`, `const` and `let`
* What are all the data types available in JavaScript
* How to use the `if`, `if ... else` statements
* How to use comments
* How to affect values to variables
* How to use `while` and `for` loops
* How to use `break` and `continue` statements
* What is a function and how do you use functions
* What does a function that does not use any `return` statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

| Task | File |
| ---- | ---- |
| 0. First constant, first print | [0-javascript_is_amazing.js](./0-javascript_is_amazing.js) |
| 1. 3 languages | [1-multi_languages.js](./1-multi_languages.js) |
| 2. Arguments | [2-arguments.js](./2-arguments.js) |
| 3. Value of my argument | [3-value_argument.js](./3-value_argument.js) |
| 4. Create a sentence | [4-concat.js](./4-concat.js) |
| 5. An Integer | [5-to_integer.js](./5-to_integer.js) |
| 6. Loop to languages | [6-multi_languages_loop.js](./6-multi_languages_loop.js) |
| 7. I love C | [7-multi_c.js](./7-multi_c.js) |
| 8. Square | [8-square.js](./8-square.js) |
| 9. Add | [9-add.js](./9-add.js) |
| 10. Factorial | [10-factorial.js](./10-factorial.js) |
| 11. Second biggest! | [11-second_biggest.js](./11-second_biggest.js) |
| 12. Object | [12-object.js](./12-object.js) |
| 13. Add file | [13-add.js](./13-add.js) |

## Tasks
### 0. First constant, first print
* A script that prints “JavaScript is amazing”:
	* You must create a constant variable called `myVar` with the value “JavaScript is amazing”
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 1. 3 languages
* A script that prints 3 lines:
	* The first line: "C is fun"
	* The second line: "Python is cool"
	* The third line: "JavaScript is amazing"
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 2. Arguments
* A script that prints a message depending on the number of arguments passed:
	* If no arguments are passed to the script, print "No argument"
	* If only one argument is passed to the script, print "Argument found"
	* Otherwise, print "Arguments found"
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 3. Value of my argument
* A script that prints the first argument passed to it:
	* If no arguments are passed to the script, print"No argument"
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
	* You are not allowed to use `length`
### 4. Create a sentence
* A script that prints two arguments passed to it, in the following format:"is"
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 5. An Integer
* A script that prints `My number: <first argument converted in integer>` if the first argument can be converted to an integer:
	* If the argument can't be converted to an integer, print"Not a number"
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
	* You are not allowed to use `try/catch`
### 6. Loop to languages
* A script that prints 3 lines:(like [1-multi_languages.js](./1-multi_languages.js)) but by using an array of strings and a loop 
	* The first line:"C is fun"
	* The second line:"Python is cool"
	* The third line:"JavaScript is amazing"
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
	* You are not allowed to use any `if/else` statement
	* You can use only one `console.log`
	* You must use a loop (`while`,`for`, etc.)
### 7. I love C
* A script that prints `x` times "C is fun"
	* Where `x` is the first argument of the script
	* If the first argument can't be converted to an integer, print"Missing number of occurrences”
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
	* You can use only two `console.log`
	* You must use a loop(`while`,`for`, etc.)
### 8. Square
* A script that prints a square
	* The first argument is the size of the square
	* If the first argument can't be converted to an integer, print "Missing size"
	* You must use the character `X` to print the square
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
	* You must use a loop (`while`,`for`, etc.)
### 9. Add
* A script that prints the addition of 2 integers
	* The first argument is the first integer
	* The second argument is the second integer
	* You have to define a function with this prototype: `function add(a, b)`
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 10. Factorial
* A script that computes and prints a factorial
	* The first argument is integer (argument can be cast as integer) used for computing the factorial
	* Factorial of `NaN` is `1`
	* You must do it recursively
	* You must use a function
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 11. Second biggest!
* A script that searches the second biggest integer in the list of arguments.
	* You can assume all arguments can be converted to integer
	* If no argument passed, print `0`
	* If the number of arguments is 1, print `0`
	* You must use `console.log(...)` to print all output
	* You are not allowed to use `var`
### 12. Object
* Update given script to replace the value `12` with `89`:
	* You are not allowed to use `var`
### 13. Add file
* A function that returns the addition of 2 integers.
	* The function must be visible from outside
	* The name of the function must be `add`
	* You are not allowed to use `var`
