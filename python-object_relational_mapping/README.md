Python - Object-relational Mapping Project
Python Badge

Project Overview:

Welcome to the Object-relational Mapping project! In this project, you will explore the integration of two exciting worlds: Python and Databases. The primary goal is to establish a connection between your Python code and a MySQL database. This will be accomplished in two phases:

Using the MySQLdb module to connect to a MySQL database and execute SQL queries.
Utilizing the SQLAlchemy module, which acts as an Object-Relational Mapper (ORM), abstracting the storage layer from your code.
Through this project, you'll understand the benefits of using ORM, eliminate the need for direct SQL queries, and achieve greater flexibility in managing your data.

Table of Contents:

Background Context
Resources
Learning Objectives
Requirements
Project Tasks
Task 0: Get all states
Task 1: Filter states
Task 2: Filter states by user input
Task 3: SQL Injection...
Task 4: Cities by states
Task 5: All cities by state
Task 6: First state model
Task 7: All states via SQLAlchemy
Task 8: First state
Task 9: Contains a
Background Context:

This project bridges the gap between Databases and Python, showcasing the power of Object-Relational Mapping. You'll learn how to establish connections, execute queries, and work with databases using Python. The first part employs the MySQLdb module for direct interaction, while the second part utilizes the SQLAlchemy module to abstract database interactions.

Resources:

To successfully complete this project, please consult the following resources:

Object-relational mappers
mysqlclient/MySQLdb documentation
MySQLdb tutorial
SQLAlchemy tutorial
Introduction to SQLAlchemy
Flask SQLAlchemy
10 common stumbling blocks for SQLAlchemy newbies
Python SQLAlchemy Cheatsheet
SQLAlchemy ORM Tutorial for Python Developers
Learning Objectives:

By completing this project, you will achieve the following learning objectives:

Understand the power of Python programming in database interactions.
Connect to a MySQL database from a Python script using the MySQLdb module.
Execute SQL queries to select and insert rows in a MySQL table.
Grasp the concept of Object-Relational Mapping (ORM) and its benefits.
Map a Python Class to a MySQL table using the SQLAlchemy module.
Requirements:

Recommended editor: Visual Studio Code.
All files will be executed on Ubuntu 20.04 LTS using Python 3.4.3.
The project requires the use of MySQLdb version 1.3.x and SQLAlchemy version 1.2.x.
All files must end with a newline character.
A README.md file at the root of the project folder is mandatory.
Code should adhere to PEP 8 style guidelines (version 1.7.*).
All modules, classes, and functions must have appropriate documentation explaining their purpose.
Documentation should be comprehensive and provide a clear understanding of the module, class, or method's functionality.
Use of the execute function with SQLAlchemy is not allowed.
Project Tasks:

The project consists of multiple tasks, each building on the previous one. You will be working with different Python scripts to complete these tasks. Below is a summary of each task:

Task 0: Get all states
Write a script that lists all states from the hbtn_0e_0_usa database using the MySQLdb module.

Task 1: Filter states
Write a script that lists all states with a name starting with 'N' from the hbtn_0e_0_usa database using the MySQLdb module.

Task 2: Filter states by user input
Write a script that takes a state name as an argument and displays all values in the states table that match the argument using the MySQLdb module.

Task 3: SQL Injection...
Enhance the previous script to guard against SQL injection attacks.

Task 4: Cities by states
Write a script that lists all cities from the hbtn_0e_4_usa database using the SQLAlchemy module.

Task 5: All cities by state
Write a script that takes the name of a state as an argument and lists all cities of that state using the SQLAlchemy module.

Task 6: First state model
Define a State class and create an instance of Base using SQLAlchemy.

Task 7: All states via SQLAlchemy
Write a script that lists all State objects from the hbtn_0e_6_usa database using the SQLAlchemy module.

Task 8: First state
Write a script that prints the first State object from the hbtn_0e_6_usa database using the SQLAlchemy module.

Task 9: Contains a
Write a script that lists all State objects from the hbtn_0e_6_usa database containing the letter 'a' using the SQLAlchemy module.

Feel free to dive into each task's respective Python script for further details and implementation specifics.

This project will provide you with valuable insights into the world of Object-Relational Mapping and the efficient utilization of databases in your Python applications. Good luck and enjoy the journey!