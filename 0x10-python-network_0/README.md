# 0x10. Python - Network #0

## Learning Objectives

### General

* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

| Task | File |
| ---- | ---- |
| 0. cURL body size | [0-body_size.sh](./0-body_size.sh) |
| 1. cURL to the end | [1-body.sh](./1-body.sh) |
| 2. cURL Method | [2-delete.sh](./2-delete.sh) |
| 3. cURL only methods | [3-methods.sh](./3-methods.sh) |
| 4. cURL headers | [4-header.sh](./4-header.sh) |
| 5. cURL POST parameters | [5-post_params.sh](./5-post_params.sh) |
| 6. Find a peak | [6-peak.py](./6-peak.py), [6-peak.txt](./6-peak.txt) |
| 7. Only status code | [100-status_code.sh](./100-status_code.sh) |
| 8. cURL a JSON file | [101-post_json.sh](./101-post_json.sh) |

## Tasks
### 0. cURL body size
* A Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
    * The size must be displayed in bytes
    * You have to use `curl`
### 1. cURL to the end
* A Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
    * Display only body of a `200` status code response
    * You have to use `curl`
### 2. cURL Method
* A Bash script that sends a `DELETE` request to the the URL passed as the first argument and displays the body of the response
    * You have to use `curl`
### 3. cURL only methods
* A Bash script that takes in a URL and displays all HTTP methods the server will accept
    * You have to use `curl`
### 4. cURL headers
* A Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
    * A header variable `X-School-User-Id` must be sent with the value `98`
    * You have to use `curl`
### 5. cURL POST parameters
* A Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
    * A variable `email` must be sent with the value `test@gmail.com`
    * A variable `subject` must be sent with the value `I will always be here for PLD`
    * You have to use `curl`
### 7. Only status code
* A Bash script that sends a request to a URL passed as an argument and displays only the status code of the response.
    * You are not allowed to use any pipe, redirection, etc.
    * You are not allowed to use `;` and `&&`
    * You have to use `curl`
### 8. cURL a JSON File
* A Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
    * Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
    * You have to use `curl`
