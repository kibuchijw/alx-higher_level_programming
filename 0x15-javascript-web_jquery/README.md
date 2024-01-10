# 0x15. JavaScript - Web jQuery

## Learning Objectives

### General

- Why JQuery make front-end programming so easy (don’t forget to tweet today, with the hashtag #ilovejquery :))
- How to select HTML elements in JavaScript
- How to select HTML elements with JQuery
- What are differences between `ID`,`class` and`tag name` selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a `GET` request with JQuery Ajax
- How to make a `POST` request with JQuery Ajax
- How to listen/bind to DOM events

| Task                            | File                             |
| ------------------------------- | -------------------------------- |
| 0. No JQuery                    | [0-script.js](./0-script.js)     |
| 1. With JQuery                  | [1-script.js](./1-script.js)     |
| 2. Click and turn red           | [2-script.js](./2-script.js)     |
| 3. Add `.red` class             | [3-script.js](./3-script.js)     |
| 4. Toggle classes               | [4-script.js](./4-script.js)     |
| 5. List of elements             | [5-script.js](./5-script.js)     |
| 6. Change the text              | [6-script.js](./6-script.js)     |
| 7. Star wars character          | [7-script.js](./7-script.js)     |
| 8. Star Wars movies             | [8-script.js](./8-script.js)     |
| 9. Say Hello!                   | [9-script.js](./9-script.js)     |
| 10. No jQuery - document loaded | [100-script.js](./100-script.js) |
| 11. List, add, remove           | [101-script.js](./101-script.js) |
| 12. Say hello to everybody!     | [102-script.js](./102-script.js) |

## Tasks

### 0. No JQuery

- Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
  - You must use `document.querySelector` to select the HTML tag
  - You can’t use the JQuery API
- Please test with this HTML file in your browser:

### 1. With JQuery

- Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API
- Please test with this HTML file in your browser:

### 2. Click and turn red

- Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API
- Please test with this HTML file in your browser:

### 3. Add `.red` class

- Write a JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API
- Please test with this HTML file in your browser:

### 4. Toggle classes

- Write a JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:
  - The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
  - If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API

### 5. List of elements

- Write a JavaScript script that adds a `<li>` element to a list when the user clicks on the tag `DIV#add_item`:
  - The new element must be: `<li>Item</li>`
  - The new element must be added to `UL.my_list`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API

### 6. Change the text

- Write a JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API

### 7. Star wars character

- Write a JavaScript script that fetches the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`
  - The name must be displayed in the HTML tag `DIV#character`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API

### 8. Star Wars movies

- Write a JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`
  - All movie titles must be list in the HTML tag `UL#list_movies`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API

### 9. Say Hello!

- Write a JavaScript script that fetches from `https://hellosalut.stefanbohacek.dev/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello.`
  - The translation of “hello” must be displayed in the HTML tag `DIV#hello`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API
  - Your script must work when it is imported from the `<head>` tag

### 10. No jQuery - document loaded

- Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
  - You must use `document.querySelector` to select the HTML tag
  - You can’t use the jQuery API
  - Note: Your script must be imported from the `<head>` tag, not at the end of the HTML

### 11. List, add, remove

- Write a JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:

  - The new element must be: `<li>Item</li>`
  - The new element must be added to `UL.my_list`
  - When the user clicks on `DIV#add_item`: a new element is added to the list
  - When the user clicks on `DIV#remove_item`: the last element is removed from the list
  - When the user clicks on `DIV#clear_list`: all elements of the list are removed
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API
  - You script must work when it imported from the `HEAD` tag

### 12. Say hello to everybody!

- Write a JavaScript script that fetches and prints how to say “Hello” depending on the language
  - You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
  - The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
  - The translation must be fetched when the user clicks on `INPUT#btn_translate`
  - The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
  - You can’t use `document.querySelector` to select the HTML tag
  - You must use the JQuery API
  - You script must work when imported from the `<head>` tag
