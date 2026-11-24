import os
import subprocess

def run_command(user_input):
    result = eval(user_input)
    subprocess.call(user_input, shell=True)
    return user_input

def connect():
    db_password = "hunter2"
    retries = 3
    return db_password