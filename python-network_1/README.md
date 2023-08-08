# Python - Network

![Python - Network](https://img.shields.io/badge/Python-Network-orange)

This project covers various aspects of network communication using Python. It includes scripts to perform HTTP requests, interact with web servers, and utilize the `requests` library for making network calls.

## Learning Objectives

At the end of this project, you will be able to explain:

- What a URL is
- What HTTP is
- How to read a URL
- The components of an HTTP URL
- How to work with domain names and sub-domains
- How to define a port number in a URL
- What a query string is
- The concepts of HTTP requests and responses
- The significance of HTTP headers and message body
- Different HTTP request methods
- HTTP response status codes
- The concept of HTTP Cookies
- How to make requests using `cURL`
- How internet resources can be fetched using `urllib` and `requests`
- How to work with JSON resources from external services

## Requirements

- Python 3 (version 3.4.3)
- Recommended editor: Visual Studio Code
- PEP 8 style (version 1.7.*) is followed
- All files should end with a new line
- A README.md file at the root of the project folder is mandatory
- All modules, classes, and functions must be documented

## Tasks

### 0. What's my status? #1
Write a Python script that fetches the status of `https://alu-intranet.hbtn.io/status`.

### 1. Response header value #1
Write a Python script that takes a URL, sends a request, and displays the value of the `X-Request-Id` header in the response.

### 2. POST an email #1
Write a Python script that sends a POST request to a URL with an email as a parameter and displays the response body.

### 3. Error code #1
Write a Python script that sends a request to a URL and displays the body of the response. If the HTTP status code is greater than or equal to 400, display an error message.

### 4. Search API
Write a Python script that takes a letter and sends a POST request to search for a user using the GitHub API. Display user information if found.

### 5. My GitHub!
Write a Python script that uses the GitHub API to display your user ID using Basic Authentication with a personal access token.

## Usage

Each task has a corresponding Python script file. You can run these scripts to see their functionality in action.

```bash
./0-hbtn_status.py
./1-hbtn_header.py <URL>
./2-post_email.py <URL> <email>
./4-error_code.py <URL>
./5-json_api.py <letter>
./6-my_github.py <username> <password>
