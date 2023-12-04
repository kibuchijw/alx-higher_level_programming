# 0x11. Python - Network #1

## Learning Objectives

### General

* How to fetch internet resources with the Python package `urllib`
* How to decode `urllib` body response
* How to use the Python package `requests` #requestsiswaysimplerthanurllib
* How to make HTTP `GET` request
* How to make HTTP `POST`/`PUT`/etc. request
* How to fetch JSON resources
* How to manipulate data from an external service

| Task | File |
| ---- | ---- |
| 0. What's my status? #0 | [0-hbtn_status.py](./0-hbtn_status.py) |
| 1. Response header value #0 | [1-hbtn_header.py](./1-hbtn_header.py) |
| 2. POST an email #0 | [2-post_email.py](./2-post_email.py) |
| 3. Error code #0 | [3-error_code.py](./3-error_code.py) |
| 4. What's my status? #1 | [4-hbtn_status.py](./4-hbtn_status.py) |
| 5. Response header value #1 | [5-hbtn_header.py](./5-hbtn_header.py) |
| 6. POST an email #1 | [6-post_email.py](./6-post_email.py) |
| 7. Error code #1 | [7-error_code.py](./7-error_code.py) |

## Tasks
### 0. What's my status? #0
* A Python script that fetches `https://alx-intranet.hbtn.io/status`
    * You must use the package `urllib`
    * You are not allowed to import any packages other than `urllib`
    * The body of the response must be displayed like the example given (tabulation before `-`)
    * You must use a `with` statement
### 1. Response header value #0
* A Python script that takes in a URL,sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response.
    * You must use the packages `urllib` and `sys`
    * You are not allowed to import packages other than `urllib` and `sys`
    * The value of this variable is different for each request
    * You don't need to check arguments passed to the script(number of type)
    * You must use a `with` statement
### 2. POST an email #0
* A Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response(decoded in `utf-8`)
    * The email must be sent in the `email` variable
    * You must use the packages `urllib` and `sys`
    * You are not allowed to import packages other than `urllib` and `sys`
    * You don't need to check arguments passed to the script(number of type)
    * You must use the `with` statement
### 3. Error code #0
* A Python script that takes in a URL, sends a request to the URL and displays the body of the response(decoded in `utf-8`).
    * You have to manage `urllib.error.HTTPError` exceptions and print: `Error code:` folowed by the HTTP status code
    * You must use the packages `urllib` and `sys`
    * You are not allowed to import other packages than `urllib` and `sys`
    * You don't need to check arguments passed to the script(number or type)
    * You must use the `with` statement
### 4. What's my status? #1
* A Python script that fetches `https://alx-intranet.hbtn.io/status`
    * You must use the package `requests`
    * You are not allowed to import packages other than `requests`
    * The body of the response must be displayed as per example given(tabulation before `-`)
### 5. Response header value #1
* A Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header
    * You must use the packages `requests` and `sys`
    * You are not allowed to import other packages than `requests` and `sys`
    * The value of this variable is different for each request
    * You don't need to check script arguments (number and type)
### 6. POST an email #1
* A Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response.
    * The email must be sent in the variable `email`
    * You must use the package `requests` and `sys`
    * You are not allowed to import packages other than `requests` and `sys`
    * You don't need to erro check arguments passed to the script(number or type)
### 7. Error code #1
* A Python script that takes in a URL, sends a request to the URL and displays the body of the response.
    * If the HTTP status code is greater than or equal to 400, print: `Erro code:` followed by the value of the HTTP status code
    * You must use the packages `requests` and `sys`
    * You are not allowed to import packages other than `requests` and `sys`
    * You don't need to check arguments passed to the script (number or type)
