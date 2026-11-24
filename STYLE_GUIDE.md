## Secrets in code
rules: B105, B106, B107
Never write passwords or tokens in code. Read them with os.environ[...], not os.getenv, and say which variable to use.

## SQL queries
rules: B608
Use named placeholders like :name with a dict of values. Never use f-strings, string joining or %s.

## Network calls
rules: B113
Every requests call must set timeout=5. Never use a longer timeout.