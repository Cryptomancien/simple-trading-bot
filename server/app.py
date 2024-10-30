import pprint

from flask import Flask, render_template
from services.database import db

app = Flask(__name__)


@app.get("/")
def index():
    cycles = db.find().sort("_id", -1)
    cycles_count = db.estimated_document_count()
    cycles_completed_count = db.count_documents({
        "status": "completed"
    })
    cycles_completed = db.find({
        "status": "completed"
    })

    # stats
    buy_total = 0
    sell_total = 0

    for cycle in cycles_completed:
        buy = float(cycle['order_buy_price']) * float(cycle['order_buy_quantity'])
        sell = float(cycle['order_sell_price']) * float(cycle['order_sell_quantity'])
        buy_total += buy
        sell_total += sell

    if sell_total > 0:
        percent = (sell_total - buy_total) / buy_total * 100
    else:
        percent = 0

    return render_template(
        "index.html",
        cycles=cycles,
        cycles_completed_count=cycles_completed_count,
        cycles_count=cycles_count,
        percent=percent,
        buy_total=buy_total,
        sell_total=sell_total,
        gain_abs="{:.2f}".format(sell_total - buy_total) + " $"
    )


def __main__():
    app.run(debug=True, port=8080)
