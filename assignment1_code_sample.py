"""
Assignment 2 Code Scanning (Assignment 1 Code Example)
"""

import subprocess
import requests
import pymysql

db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    """Prompt user for their name and return it."""
    user_input = input("Enter your name: ")
    return user_input


def send_email(to, subject, body):
    """Send an email safely using subprocess without shell=True."""
    subprocess.run(
        ["mail", "-s", subject, to],
        input=body.encode("utf-8"),
        check=True,
    )


def get_data():
    """Fetch data from API safely using requests."""
    url = "http://insecure-api.com/get-data"
    # validate URL scheme
    if not url.startswith(("http://", "https://")):
        raise ValueError("Invalid URL scheme")
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def save_to_db(data_param):
    """Save data to the database using parameterized query."""
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    cursor.execute(query, (data_param, "Another Value"))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == "__main__":
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email("admin@example.com", "User Input", user_input)