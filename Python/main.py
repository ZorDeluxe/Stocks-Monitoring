"""
Main.py
"""
from stock import Stock
from Quantitive.Benjamin import Benjamin
from Quantitive.DCF import DCF

import csv
if __name__ == "__main__":
    stocks = ['GOOG', 'MSFT', 'TSLA', 'AAPL', 'AIR.NZ', 'AMZN', 'ANZ.NZ', 'C', 'CROX', 'ENPH', 'INTC', 'META', 'NKE', 'NVDA', 'PYPL', 'PG', 'CRM', 'SPK.NZ', 'DIS']
    stock = 'MSFT'
    # Benjamin
    # for stock in stocks:
    i = Benjamin(stock, True)
    j = DCF(stock)
    purchase = i.evaluate(25)
    purchase2 = j.evaluate(25)
    print(stock)
    print(f'{i.currentPrice:.2f} | Intrinsic Value: {i.intrinsic_value:.2f} | Acceptable Buy Price: {i.accept_buy_price:.2f} | Buy: {purchase} ')
    print(f'{j.currentPrice:.2f} | Intrinsic Value: {j.intrinsic_value:.2f} | Acceptable Buy Price: {j.accept_buy_price:.2f} | Buy: {purchase2} ')