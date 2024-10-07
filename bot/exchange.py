from os import getenv
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from requests import get, post
from services.logger import log

load_dotenv()

base_url = 'https://api.xeggex.com/api/v2'

auth = HTTPBasicAuth(
    getenv("API_PUBLIC"),
    getenv("API_SECRET")
)


def get_last_price():
    try:
        url = base_url + '/market/get by symbol'.replace(' ', '') + '/BTC_USDT'
        response = get(url)
        return response.json()
    except Exception as e:
        log(message=str(e), level="error")
        print(e)


def get_balances():
    try:
        url = base_url + '/balances'
        response = get(
            url=url,
            auth=auth
        )
        return response.json()
    except Exception as e:
        log(message=str(e), level="error")
        print(e)


def create_order(symbol: str, side: str, price: float, quantity: float):
    try:
        url = base_url + '/create order'.replace(' ', '')
        response = post(
            url=url,
            auth=auth,
            data={
                'symbol': symbol,
                'side': side,
                'price': price,
                'quantity': quantity
            }
        )
        return response.json()
    except Exception as e:
        log(str(e), 'error')
        print(e)


def get_order(order_id: str):
    try:
        url = base_url + '/get order'.replace(' ', '') + '/' + order_id
        response = get(
            url=url,
            auth=auth,
        )
        return response.json()
    except Exception as e:
        log(str(e), 'error')
        print(e)
