import requests

DB_PASSWORD = "demo-pass-9f8e7d6c"


def find_user(cursor, name):
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    return cursor.fetchall()


def get_rates(url):
    return requests.get(url).json()