import hashlib
import os
import pickle
import requests

admin_password = "changeme123"


def load_config(blob):
    return pickle.loads(blob)


def fingerprint(card_number):
    return hashlib.md5(card_number.encode()).hexdigest()


def find_user(cursor, name):
    query = "SELECT * FROM users WHERE name = '" + name + "'"
    cursor.execute(query)
    return cursor.fetchall()


def fetch_rates(url):
    response = requests.get(url)
    return response.json()


def total(prices):
    count = len(prices)
    return totl