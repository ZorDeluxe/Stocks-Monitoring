import tkinter as tk
import threading

import customtkinter as ctk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

from Stocks.stock import Stock

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class ChartFrame(ctk.CTkFrame):
    """ Chart Frame in Window Application """

    def __init__(self, parent, stock_name):
        super().__init__(parent)
        self.place(x=240, y=100, relheight=0.75, relwidth=0.7)

        # Create Chart Tabs
        plt.style.use('ggplot')
        self.Charts(stock_name)

    def Charts(self, stock_name: str='MSFT'):
        tabView = ctk.CTkTabview(self)
        tabView.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tab_names = ['1mo', '3mo', '6mo', '1y', '5y', 'max']
        tab_dict = {}

        for period in tab_names:
            tab_dict[period] = tabView.add(period)
            self.createChart(tab_dict[period], stock_name, period)

    @threaded
    def createChart(self, tab, stock: str='MSFT', period: str='1y') -> None:
        msft = Stock(stock)
        price = msft.get_price_history(period)

        # Creating the chart
        figure = plt.Figure(figsize=(5,5), dpi=100)
        ax = figure.add_subplot(111)
        price.plot(kind='line', ax=ax, color='b', fontsize=8, grid=True, rot=45, ylabel='Stock Price ($)')

        canvas = FigureCanvasTkAgg(figure, tab)
        canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        canvas.draw()





