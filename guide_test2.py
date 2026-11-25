import requests

DB_PASSWORD = "demo-pass-1a2b3c4d"


def find_user(cursor, name):
    query = f"SELECT * FROM users WHERE name = '{name}'"
    cursor.execute(query)
    return cursor.fetchall()


def get_rates(url):
    return requests.get(url).json()


