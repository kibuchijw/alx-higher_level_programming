# 0x14. JavaScript - Web scraping

## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use `request`and fetch API
* How to read and write a file using `fs`module

| Task | File |
| ---- | ---- |
| 0. Readme | [0-readme.js](./0-readme.js) |
| 1. Write me | [1-writeme.js](./1-writeme.js) |
| 2. Status code | [2-statuscode.js](./2-statuscode.js) |
| 3. Star wars movie title | [3-starwars_title.js](./3-starwars_title.js) |
| 4. Star wars Wedge Antilles | [4-starwars_count.js](./4-starwars_count.js) |

## Tasks
### 0. Readme
* Write a script that reads and prints the content of a file.
    * The first argument is the file path
    * The content of the file must be read in `utf-8`
    * If an error occurred during the reading, print the error object
### 1. Write me
* Write a script that writes a string to a file.
    * The first argument is the file path
    * The second argument is the string to write
    * The content of the file must be written in `utf-8`
    * If an error occurred during the writing, print the error object
### 2. Status code
* Write a script that displays the status code of a `GET` request.
    * The first argument is the URL to request(`GET`)
    * The status code must be printed like this: `code: <status code>`
    * You must use the module `request`
### 3. Star wars movie title
* Write a script that prints the title of a Star Wars movie where the episode number matches a given integer.
    * The first argument is the movie ID
    * You must use the [Star wars API](https://swapi-api.alx-tools.com/) with the endpoint `https://swapi-api.alx-tools.com/api/films/:id`
    * You must use the module `request`
### 4. Star wars Wedge Antilles
* Write a script that prints the number of movies where the character “Wedge Antilles” is present.
    * The first argument is the API URL of the [Star wars API](https://swapi-api.alx-tools.com/):`https://swapi-api.alx-tools.com/api/films/`
    * Wedge Antilles is character ID `18`-your script **must** use this ID for filtering the result of the API
    * You must use the module `request`
