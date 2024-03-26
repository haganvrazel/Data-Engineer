import csv
import os
from collections import defaultdict
from operator import itemgetter


def process_trades(input_file):
    trades_by_symbol = defaultdict(list)

    with open(input_file, 'r', newline='') as csvfile:
        trade_processor = csv.reader(csvfile)
        for row in trade_processor:
            timestamp, symbol, quantity, price = int(row[0]), row[1], int(row[2]), int(row[3])
            trade = (timestamp, quantity, price)
            trades_by_symbol[symbol].append(trade)

    return trades_by_symbol


def calculate_stats(trades_by_symbol):
    symbol_stats = []

    for symbol, trades in trades_by_symbol.items():
        trades.sort(key=itemgetter(0))  # Sorting trades by timestamp

        if len(trades) == 1:
            max_time_gap = 0
        else:
            max_time_gap = max(trades[i + 1][0] - trades[i][0] for i in range(len(trades) - 1))

        total_volume = sum(trade[1] for trade in trades)
        weighted_avg_price = sum(quantity * price for _, quantity, price in trades) // total_volume
        max_price = max(trade[2] for trade in trades)
        symbol_stats.append((symbol, max_time_gap, total_volume, weighted_avg_price, max_price))

    return sorted(symbol_stats, key=itemgetter(0))  # Sorting by ticker symbol


def write_output(output_file, symbol_stats):
    with open(output_file, 'w', newline='') as csvfile:
        output_writer = csv.writer(csvfile)
        for symbol_stat in symbol_stats:
            output_writer.writerow(symbol_stat)


if __name__ == "__main__":
    # Getting absolute path to root directory
    root_dir = os.path.dirname(os.path.abspath(__file__))

    input_file = os.path.join(root_dir, '..', 'input.csv')
    output_file = 'output.csv'

    trades_by_symbol = process_trades(input_file)
    symbol_stats = calculate_stats(trades_by_symbol)
    write_output(output_file, symbol_stats)
