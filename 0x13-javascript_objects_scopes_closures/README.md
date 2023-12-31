# 0x13. JavaScript - Objects, Scopes and Closures

## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What `this` means
* What `undefined` means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

| Task | File |
| ---- | ---- |
| 0. Rectangle #0 | [0-rectangle.js](./0-rectangle.js) |
| 1. Rectangle #1 | [1-rectangle.js](./1-rectangle.js) |
| 2. Rectangle #2 | [2-rectangle.js](./2-rectangle.js) |
| 3. Rectangle #3 | [3-rectangle.js](./3-rectangle.js) |
| 4. Rectangle #4 | [4-rectangle.js](./4-rectangle.js) |
| 5. Square #0 | [5-square.js](./5-square.js) |
| 6. Square #1 | [6-square.js](./6-square.js) |
| 7. Occurrences | [7-occurrences.js](./7-occurrences.js) |
| 8. Esrever | [8-esrever.js](./8-esrever.js) |
| 9. Log me | [9-logme.js](./9-logme.js) |

## Tasks
### 0. Rectangle #0
* An empty class `Rectangle` that defines a rectangle:
	* You must use the `class` notation for defining class
### 1. Rectangle #1
* A class `Rectangle` that defines a rectangle:
	* You must use the `class` notation for defining class
	* The constructor must take 2 arguments `w` and `h`
	* Iitialize the instace attribute `width` with the value of `w`
	* Initialize the instance attribute `height` with the value of `h`
### 2. Rectangle #2
* A class `Rectangle` that defines a rectangle:
	* You must use the `class` notation for defining class
	* The constructor must take 2 arguments `w` and `h`
	* Initialize the instance attribute `width` with the value of `w`
	* Initialize the instance attribute `height` with the value of `h`
	* If `w` or `h` is equal to 0 or not a positive integer, create an empty object
### 3. Rectangle #3
* A class `Rectangle` that defines a rectangle:
	* You must use the `class` notation for defining class
	* The constructor must take 2 arguments: `w` and `h`
	* Initialize the instance attribute `width` with the value of `w`
	* Initialize the instance attribute `height` with the value of `h`
	* If `w` of `h` is equal to 0 or not a positive integer, create an empty object
	* Create an instance method called `print()` that prints the rectangle using the character `X`
### 4. Rectangle #4
* A class `Rectangle` that defines a rectangle:
	* You must use the `class` notation for defining class
	* The constructor must take 2 arguments: `w` and `h`
	* Initialize the instance attribute `width` with the value of `w`
	* Initialize the instance attribute `height` with the value of `h`
	* If `w` of `h` is equal to 0 or not a positive integer, create an empty object
	* Create an instance method called `print()` that prints the rectangle using the character `X`
	* Create an instance method called `rotate()` that exchanges the `width` and the `height` of the rectangle
	* Create an instance method called `double()` that multiplies the `width` and the `height` of the rectangle by 2
### 5. Square #0
* A class `Square` that defines a square and inherits from `Rectangle` of `4-rectangle.js`:
	* You must use the `class` notation for defining class and `extends`
	* The constructor must take 1 argument: `size`
	* The constructor of `Rectangle` must be called(by using `super()`)
### 6. Square #1
* A class `Square` that defines a square and inherits from `Square` of `5-square.js`:
	* You must use the `class` notation for defining class and `extends`
	* Create an instance method called `charPrint(c)` that prints the rectangle using the character `c`
		* If `c` is `undefined`, use the character `X`
### 7. Occurrences
* A function that returns the number of occurrences in a list:
	* Prototype: `exports.nbOccurences = function (list, searchElement)`
### 8. Esrever
* A function that returns the reversed version of a list:
	* Prototype: `exports.esrever = function (list)`
	* You are not allowed to use the built-in method `reverse`
### 9. Log me
* A function that prints the number of arguments already printed and the new argument value.
	* Prototype: `exports.logMe = function (item)`
	* Output format: `<number arguments already printed>: <current argument value>`
