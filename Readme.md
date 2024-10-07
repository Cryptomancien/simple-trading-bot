# Simple Trading Bot

![alt text](https://pbs.twimg.com/media/GYvhSB1WcAA1Z61?format=png&name=medium "Title")


## Required

- Git
- Python 3.12 +
- Poetry
- MongoDB

## Install

``` bash
git clone https://github.com/cryptomancien/simple-trading-bot
cd simple-trading-bot
poetry install
cp .env.example .env
```

## Config

- Create an account on XeggeX
- Enable 2FA
- Create API key
- Fill USDT
- Change keys in .env

## Launch

``` bash
# Check requirement
poetry run main.py -c

# Start new cycle
poetry run main.py -n

# Update running cycles
poetry run main.py -u

# Start local server, port 8080
poetry run main.py -s
```
