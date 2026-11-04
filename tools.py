import json
import os
import secrets
import subprocess
import sys

import requests
import yaml

TOKEN = "demo-token-1a2b3c4d5e6f"


def run_git(args):
    result = subprocess.run(["git", *args], capture_output=True, text=True, check=True)
    return result.stdout


def run_shell(command):
    return subprocess.call(command, shell=True)


def new_token():
    return secrets.token_hex(16)


def load_config(text):
    return yaml.safe_load(text)


def read_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def read_setting(name):
    return os.environ.get(name, "")


def parse_port(text):
    try:
        return int(text)
    except ValueError:
        return 0


def send(url, data):
    return requests.post(url, data=data, timeout=10, verify=False)


def pick_mode(mode):
    if mode is "fast":
        return 1
    return 0


def percent(part, total):
    return part / total * 10