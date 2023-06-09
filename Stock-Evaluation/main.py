"""
Main.py
"""

from Quantitive.Benjamin import Benjamin
if __name__ == "__main__":
    stocks = ['GOOG', 'MSFT', 'TSLA', 'AAPL', 'AIR.NZ', 'AMZN', 'ANZ.NZ', 'C', 'CROX', 'ENPH', 'INTC', 'META', 'NKE', 'NVDA', 'PYPL', 'PG', 'CRM', 'SPK.NZ', 'DIS']
    for stock in stocks:
        i = Benjamin(stock, True)
        purchase = i.evaluate(25)

        print(f'{i.name}\nCurrent Price: {i.currentPrice:.2f} | Intrinsic Value: {i.intrinsic_value:.2f} | Acceptable Buy Price: {i.accept_buy_price:.2f} | Buy: {purchase} ')
