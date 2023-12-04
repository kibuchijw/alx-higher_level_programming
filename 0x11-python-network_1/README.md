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
