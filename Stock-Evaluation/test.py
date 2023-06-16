"""
Main.py
"""
from Quantitive.Benjamin import Benjamin
from Quantitive.Lynch import Lynch

if __name__ == "__main__":
    stocks = ['GOOG', 'MSFT', 'TSLA', 'AAPL', 'AIR.NZ', 'AMZN', 'ANZ.NZ', 'C', 'CROX', 'ENPH', 'INTC', 'META', 'NKE', 'NVDA', 'PYPL', 'PG', 'CRM', 'SPK.NZ', 'DIS']
    for stock in stocks:
        xx = Lynch(stock)
        value, comment = xx.evaluate()
        print(f'{xx.name}| Fair Value {value} -> {comment}')


