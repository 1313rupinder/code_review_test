## Secrets in code
rules: B105, B106, B107
Never write passwords or tokens in code. Read them from environment variables and say which variable to use.

## SQL queries
rules: B608
Always use parameterized queries. Never build SQL with f-strings or string joining.

## Network calls
rules: B113
Every requests call must set timeout=10 or lower.