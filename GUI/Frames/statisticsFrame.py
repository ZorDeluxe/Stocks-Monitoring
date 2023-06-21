import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

from Stocks.stock import Stock

class StatsFrame(ctk.CTkFrame):
    """ Creates the Statistics Preview of Stocks """

    def __init__(self, parent, stock_name):
        """ Instatiate the Statistics Frame """
        stock = Stock(stock_name)           # Gets stock information

        super().__init__(parent,            # Creates the frame
                         height=598, 
                         width=240,
                         border_width=2)
        self.place(x=0, y=102)

        ####################################################
        #                     Heading                      #
        ####################################################
        nameLabel = ctk.CTkLabel(self, 
                                 text=stock_name,
                                 width=236,
                                 height=50,
                                 justify="center",
                                 font=('Arial', 20))
        nameLabel.place(x=2, y=5)

        # Current Price
        priceLabel = ctk.CTkLabel(self,
                                  text="Current Price",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        priceLabel.place(x=2, y=60)

        price = ctk.CTkLabel(self, 
                             text=stock.get_currentPrice(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        price.place(x=2, y=80)

        priceDiv = ttk.Separator(self, 
                                 orient="horizontal")
        priceDiv.place(x=24, y=110, relwidth=0.8)

        # EPS
        epsLabel = ctk.CTkLabel(self,
                                text="Earnings Per Share",
                                width=236,
                                height=20,
                                justify="center",
                                font=("Arial", 15))
        epsLabel.place(x=2, y=120)

        eps = ctk.CTkLabel(self, 
                             text=stock.get_EPS(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        eps.place(x=2, y=140)

        epsDiv = ttk.Separator(self, 
                                 orient="horizontal")
        epsDiv.place(x=24, y=170, relwidth=0.8)



