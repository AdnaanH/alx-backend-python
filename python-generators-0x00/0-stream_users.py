#!/usr/bin/python3
import mysql.connector
from seed import connect_to_prodev

def stream_users():
    """
    Generator that yields one user row at a time from the user_data table.
    """
    connection = connect_to_prodev()
    cursor = connection.cursor(dictionary=True)

    # Execute query
    cursor.execute("SELECT * FROM user_data")

    # Yield rows one by one using a single loop
    for row in cursor:
        yield row

    # Cleanup
    cursor.close()
    connection.close()
