import hashlib
import math
import os
import random
import subprocess

import requests
import yaml

DEFAULT_PWD = "Passw0rd!"


def checksum(data):
    return hashlib.md5(data, usedforsecurity=False).hexdigest()


def shuffled(items):
    items = list(items)
    random.shuffle(items)
    return items


def current_branch():
    out = subprocess.run(["git", "branch", "--show-current"], capture_output=True, text=True, check=True)
    return out.stdout.strip()


def find_user(conn, name):
    return conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()


def fetch(url):
    return requests.get(url, timeout=10).json()


def db_password():
    return os.environ["DB_PASSWORD"]


def load_settings(text):
    return yaml.load(text)


def last_n(values, n):
    return values[len(values) - n + 1:]