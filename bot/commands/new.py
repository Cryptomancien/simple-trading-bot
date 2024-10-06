import bot.exchange as exchange
from os import getenv
from dotenv import load_dotenv
from bot.order_db import Status, order_db
from services.database import db
from termcolor import cprint, colored
from pprint import pp

load_dotenv()


def get_trade_amount(total_available: float, percent: int) -> float:
    return (percent * total_available) / 100


def run():
    last_price = exchange.get_last_price()
    last_price = last_price["lastPriceNumber"]

    cprint("\n Last price: " + colored(last_price, color="green"))

    buy_offset = getenv("BUY_OFFSET") or -2000
    buy_offset = int(buy_offset)
    buy_offset = abs(buy_offset)

    sell_offset = getenv("SELL_OFFSET") or 2000
    sell_offset = int(sell_offset)
    sell_offset = abs(sell_offset)

    price_input = last_price - buy_offset
    price_output = last_price + sell_offset

    cprint("\n Price input: " + colored(price_input, color="green"))
    cprint("\n Price output: " + colored(price_output, color="green"))

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

    cprint("\n Balance USDT: " + colored(balance_usd, color="green"))

    percent = getenv("PERCENT_AVAILABLE=6") or 6
    balance_playable = get_trade_amount(balance_usd, percent)
    balance_playable = "{:.6f}".format(balance_playable / float(price_input))
    balance_playable = float(balance_playable)

    cprint("\n Balance playable: " + colored(balance_playable, color="green"))

    # execute order and store data
    # order_exchange = exchange.create_order("BTC_USDT", "buy", price=price_input, quantity=balance_playable)
    # pp(order_exchange)

    order_data = order_db
    # order_data["status"] = Status.ORDER_BUY_PLACED
    # order_data["order_buy_id"] = order_exchange["id"]
    # order_data["order_buy_price"] = order_exchange["price"]
    # order_data["order_buy_quantity"] = order_exchange["quantity"]
    # order_data["order_buy_date"] = order_exchange["createdAt"]
    order_data["TEST"] = True
    order_data = dict(order_data)


    db.insert_one(order_data)
    cprint("\n Cycle started successfully", color="light_green")