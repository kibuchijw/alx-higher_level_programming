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

| Task                  | File                         |
| --------------------- | ---------------------------- |
| 0. No JQuery          | [0-script.js](./0-script.js) |
| 1. With JQuery        | [1-script.js](./1-script.js) |
| 2. Click and turn red | [2-script.js](./2-script.js) |
| 3. Add `.red` class   | [3-script.js](./3-script.js) |
| 4. Toggle classes     | [4-script.js](./4-script.js) |
| 5. List of elements   | [5-script.js](./5-script.js) |

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
