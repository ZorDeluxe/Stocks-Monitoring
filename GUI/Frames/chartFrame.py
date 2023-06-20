import tkinter as tk
import customtkinter as ctk

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt

from Stocks.stock import Stock

class ChartFrame(ctk.CTkFrame):
    """ Chart Frame in Window Application """

    def __init__(self, parent):
        super().__init__(parent)
        self.place(x=240, y=0, relwidth=0.70, relheight=0.8)

        # Create Chart Tabs
        plt.style.use('ggplot')
        self.Charts()

    def Charts(self, stock: str='MSFT'):
        tabView = ctk.CTkTabview(self)
        tabView.pack(padx=0, pady=0, side=tk.RIGHT, fill=tk.BOTH, expand=True)

        tab_names = ['1mo', '3mo', '6mo', '1y', '5y', 'max']
        self.tab_dict = {}

        for period in tab_names:
            self.tab_dict[period] = tabView.add(period)
            self.createChart(self.tab_dict[period], stock, period)
        
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





