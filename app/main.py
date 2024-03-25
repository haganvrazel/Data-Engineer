import csv
from collections import defaultdict


def process_trades(input_file):
    trades_by_symbol = defaultdict(list)

    with open(input_file, 'r', newline='') as csvfile:
        trade_processor = csv.reader(csvfile)
        for row in trade_processor:
            timestamp, symbol, quantity, price = int(row[0]), row[1], int(row[2]), int(row[3])
            trade = (timestamp, quantity, price)
            trades_by_symbol[symbol].append(trade)

    return trades_by_symbol
