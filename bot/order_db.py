from enum import Enum


class Status(Enum):
    ORDER_BUY_PLACED = "order_buy_placed"
    ORDER_BUY_FILLED = "order_buy_filled"
    ORDER_SELL_PLACED = "order_sell_filled"
    COMPLETED = "completed"


order_db = {
    "status": None,

    "order_buy_id": None,
    "order_buy_price": None,
    "order_buy_quantity": None,
    "order_buy_date": None,

    "order_sell_id": None,
    "order_sell_price": None,
    "order_sell_quantity": None,
    "order_sell_date": None,
}
