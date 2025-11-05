"""
Assignment 2 Code Scanning (Assignment 1 Code Example)
"""

import os
from urllib.request import urlopen

import pymysql

db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    """Prompt user for their name and return it."""
    user_input_local = input("Enter your name: ")
    return user_input_local


def send_email(to, subject, body):
    """Send an email using os.system."""
    os.system(f'echo {body} | mail -s "{subject}" {to}')


def get_data():
    """Fetch data from insecure API."""
    url = "http://insecure-api.com/get-data"
    with urlopen(url) as response:
        data_local = response.read().decode()
    return data_local


def save_to_db(data_param):
    """Save data to the database."""
    query = f"INSERT INTO mytable (column1, column2) VALUES ('{data_param}', 'Another Value')"
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_input_outer = get_user_input()
    data_outer = get_data()
    save_to_db(data_outer)
    send_email("admin@example.com", "User Input", user_input_outer)
