"""
Assignment 2 Code Scanning (Assignment 1 Code Example)
"""

import subprocess

import pymysql
import requests

db_config = {"host": "mydatabase.com", "user": "admin", "password": "secret123"}


def get_user_input():
    """Prompt user for their name and return it."""
    user_name = input("Enter your name: ")
    return user_name


def send_email(to, subject, body):
    """Send an email safely using subprocess"""

    mail_cmd = ["/usr/bin/mail", "-s", subject, to]

    subprocess.run(
        mail_cmd,
        input=body.encode("utf-8"),
        check=True,
    )


def get_data():
    """Fetch data from API safely using requests."""
    url = "http://insecure-api.com/get-data"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return ""


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
