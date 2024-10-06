import bot.exchange as exchange
from os import getenv
from dotenv import load_dotenv

load_dotenv()


def get_trade_amount(total_available: float, percent: int) -> float:
    return (percent * total_available) / 100


def run():
    last_price = exchange.get_last_price()
    last_price = last_price["lastPriceNumber"]

    buy_offset = getenv("BUY_OFFSET") or -2000
    buy_offset = int(buy_offset)
    buy_offset = abs(buy_offset)

    sell_offset = getenv("SELL_OFFSET") or 2000
    sell_offset = int(sell_offset)
    sell_offset = abs(sell_offset)

    price_input = last_price - buy_offset
    price_output = last_price + sell_offset

    balances = exchange.get_balances()
    balances = filter(
        lambda balance: (
            balance['asset'] == 'BTC' or balance['asset'] == 'USDT'
        ),
        balances
    )
    balances = list(balances)

    balance_usd = balances[1]
    balance_usd = float(balance_usd['available'])

    percent = getenv("PERCENT_AVAILABLE=6") or 6
    balance_playable = get_trade_amount(balance_usd, percent)
    balance_playable = "{:.6f}".format(balance_playable / float(price_input))

