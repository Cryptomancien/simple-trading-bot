from pprint import pp
from services.database import db
from bot.order_db import Status
import bot.exchange as exchange
from bson import ObjectId
from termcolor import cprint


def update_cycle_status_by_id(cycle_id: str, status: str):
    db.update_one(
        {
            "_id": ObjectId(cycle_id)
        },
        {
            "$set": {
                "status": status
            }
        }
    )


def update_cycle_sell_price_by_id(cycle_id: str, price: str):
    db.update_one(
        {
            "_id": ObjectId(cycle_id)
        },
        {
            "$set": {
                "order_sell_price": price
            }
        }
    )


def run():
    cycles_uncompleted = db.find({
        "status": {
            "$ne": "completed"
        }
    })

    last_price = exchange.get_last_price()
    last_price = last_price["lastPriceNumber"]

    for cycle in cycles_uncompleted:
        cycle_status = cycle["status"]

        if cycle_status == Status.ORDER_BUY_PLACED.value:
            order_id = cycle["order_buy_id"]
            order = exchange.get_order(order_id)

            if order["isActive"]:
                pp(f'{order_id} order buy still active')
            else:
                update_cycle_status_by_id(
                    cycle["_id"],
                    Status.ORDER_BUY_FILLED.value
                )
                order_sell_price = cycle["order_sell_price"]
                order_sell_quantity = cycle["order_sell_quantity"]

                if float(last_price) > float(cycle["order_sell_price"]):
                    new_sell_price = cycle["order_sell_price"]
                    new_sell_price = float(new_sell_price) + 100
                    new_sell_price = str(new_sell_price)

                    update_cycle_sell_price_by_id(
                        cycle["_id"],
                        new_sell_price
                    )

                    order_sell = exchange.create_order(
                        symbol="BTC_USDT",
                        side="sell",
                        price=float(new_sell_price),
                        quantity=order_sell_quantity
                    )

                    db.update_one(
                        {
                            "_id": ObjectId(cycle["_id"])
                        },
                        {
                            "$set": {
                                "status": Status.ORDER_SELL_PLACED.value,
                                "order_sell_id": order_sell["id"],
                                "order_sell_date": order_sell["createdAt"]
                            }
                        }
                    )
        elif cycle_status == Status.ORDER_SELL_PLACED.value:
            order_id = cycle["order_sell_id"]
            order = exchange.get_order(order_id)
            if order["isActive"]:
                pp(f'{order_id} order buy still active')
            else:
                update_cycle_status_by_id(
                    cycle["_id"],
                    Status.COMPLETED.value
                )
                cprint("Cycle successfully completed", color="light_green")
