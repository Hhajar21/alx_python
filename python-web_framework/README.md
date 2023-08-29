Python Web Framework Project
Python
Flask
Status

This project focuses on building a web application using the Flask web framework. It involves creating routes, rendering templates, and handling various types of requests. The goal is to gain a better understanding of web frameworks and their functionalities.

Table of Contents
Learning Objectives
Requirements
Setup
Tasks
License
Learning Objectives
Upon completing this project, you should be able to:

Explain the concept of a web framework and its purpose.
Build a web framework using Flask.
Define routes in Flask and understand their significance.
Handle variables in routes to create dynamic content.
Utilize templates for rendering HTML responses.
Create dynamic templates using loops and conditions.
Retrieve and display data from a MySQL database in HTML.
Requirements
Python Scripts
Recommended editor: Visual Studio Code
Scripts should be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.4.3.
All files should end with a new line.
Follow the PEP 8 style guide (version 1.7).
Document all modules, classes, and functions with meaningful descriptions.
HTML/CSS Files
Recommended editor: Visual Studio Code
All files should end with a new line.
Ensure W3C compliance and validate with W3C-Validator (except for Jinja templates).
Place CSS files in the styles folder.
Store images in the images folder.
Avoid using !important or id (#...) in CSS files.
Use uppercase for all HTML tags.
Setup
To install Flask, use the following command:

bash
Copy code
$ pip3 install Flask
Tasks
The project involves the completion of several tasks, each building upon the previous one. The tasks include:

Hello Flask! - Start a Flask web application, listening on 0.0.0.0:5000, and display "Hello HBNB!" at the root route.
HBNB - Expand the web application to display "HBNB" at the route "/hbnb".
C is fun! - Extend the application to display "C " followed by text variable at "/c/<text>" route.
Python is cool! - Add "/python/<text>" route to display "Python " followed by text variable, with default value "is cool".
Is it a number? - Introduce "/number/<n>" route to display "n is a number" only if n is an integer.
Number template - Create "/number_template/<n>" route to render an HTML page with "Number: n" in an H1 tag.
Odd or even? - Extend the project with "/number_odd_or_even/<n>" route to display if n is even or odd.
Please review the individual task files for implementation details and usage instructions.

License
This project is licensed under the MIT License.