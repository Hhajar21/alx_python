#!/usr/bin/python3

# Filter States Script
# This script retrieves and lists all states with names starting with an uppercase 'N'
# from the database hbtn_0e_0_usa.

# Usage: ./1-filter_states.py <mysql_username> <mysql_password> <database_name>

# Requirements:
# - The script requires three command-line arguments: MySQL username, MySQL password, and database name.
# - It utilizes the MySQLdb module for MySQL database connectivity.
# - The script connects to a MySQL server on localhost, port 3306.
# - The results are sorted in ascending order by states.id.
# - The output displays the state ID and name in the format: (ID, 'Name').

# Example:
# ./1-filter_states.py root root hbtn_0e_0_usa
# Output:
# (4, 'New York')
# (5, 'Nevada')

if __name__ == '__main__':
    import MySQLdb
    import sys

    # Connect to the MySQL database
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Create a cursor and execute the query
    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id ASC""")

    # Fetch and display the query results
    rows = cur.fetchall()
    for row in rows:
        print(row)
