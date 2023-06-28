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
                         width=240)
        self.place(x=560, y=102)

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
        priceDiv.place(x=48, y=110, relwidth=0.6)

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
        epsDiv.place(x=48, y=170, relwidth=0.6)

        # 5 Year Growth Rate
        growthLabel = ctk.CTkLabel(self,
                                  text="Growth Estimate",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        growthLabel.place(x=2, y=180)

        growth = ctk.CTkLabel(self, 
                             text=stock.get_growthRate(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        growth.place(x=2, y=200)

        growthDiv = ttk.Separator(self, 
                                 orient="horizontal")
        growthDiv.place(x=48, y=230, relwidth=0.6)

        # Price to Earning Ratio
        peRatioLabel = ctk.CTkLabel(self,
                                  text="P/E Ratio",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        peRatioLabel.place(x=2, y=240)

        peRatio = ctk.CTkLabel(self, 
                             text=stock.get_priceToEarning(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        peRatio.place(x=2, y=260)

        peRatioDiv = ttk.Separator(self, 
                                 orient="horizontal")
        peRatioDiv.place(x=48, y=290, relwidth=0.6)

        # Price to Book Ratio
        pbRatioLabel = ctk.CTkLabel(self,
                                  text="P/B Ratio",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        pbRatioLabel.place(x=2, y=300)

        pbRatio = ctk.CTkLabel(self, 
                             text=stock.get_priceToBook(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        pbRatio.place(x=2, y=320)

        pbRatioDiv = ttk.Separator(self, 
                                 orient="horizontal")
        pbRatioDiv.place(x=48, y=350, relwidth=0.6)

        # PEG Ratio
        pegRatioLabel = ctk.CTkLabel(self,
                                  text="PEG Ratio",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        pegRatioLabel.place(x=2, y=360)

        pegRatio = ctk.CTkLabel(self, 
                             text=stock.get_pegRatio(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        pegRatio.place(x=2, y=380)

        pegRatioDiv = ttk.Separator(self, 
                                 orient="horizontal")
        pegRatioDiv.place(x=48, y=410, relwidth=0.6)

        # Debt to Equity
        deRatioLabel = ctk.CTkLabel(self,
                                  text="D/E Ratio",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        deRatioLabel.place(x=2, y=420)

        deRatio = ctk.CTkLabel(self, 
                             text=stock.get_debtToEquity(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        deRatio.place(x=2, y=440)

        deRatioDiv = ttk.Separator(self, 
                                 orient="horizontal")
        deRatioDiv.place(x=48, y=470, relwidth=0.6)

        # Dividends per share
        divLabel = ctk.CTkLabel(self,
                                  text="Dividend Per Share",
                                  width=236,
                                  height=20,
                                  justify="center",
                                  font=("Arial", 15))
        divLabel.place(x=2, y=480)

        dividend = ctk.CTkLabel(self, 
                             text=stock.get_dividendPerShare(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        dividend.place(x=2, y=500)

        dividendDiv = ttk.Separator(self, 
                                 orient="horizontal")
        dividendDiv.place(x=48, y=530, relwidth=0.6)


    def update_stats_frame(self, stock_name):
        stock = Stock(stock_name)           # Gets stock information

        nameLabel = ctk.CTkLabel(self, 
                                text=stock_name,
                                width=236,
                                height=50,
                                justify="center",
                                font=('Arial', 20))
        nameLabel.place(x=2, y=5)

        price = ctk.CTkLabel(self, 
                            text=stock.get_currentPrice(),
                            width=236,
                            height=20,
                            justify="center",
                            font=("Arial", 20),
                            text_color="#0ABAB5")
        price.place(x=2, y=80)

        eps = ctk.CTkLabel(self, 
                            text=stock.get_EPS(),
                            width=236,
                            height=20,
                            justify="center",
                            font=("Arial", 20),
                            text_color="#0ABAB5")
        eps.place(x=2, y=140)

        growth = ctk.CTkLabel(self, 
                            text=stock.get_growthRate(),
                            width=236,
                            height=20,
                            justify="center",
                            font=("Arial", 20),
                            text_color="#0ABAB5")
        growth.place(x=2, y=200)

        pbRatio = ctk.CTkLabel(self, 
                             text=stock.get_priceToBook(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        pbRatio.place(x=2, y=320)

        pegRatio = ctk.CTkLabel(self, 
                             text=stock.get_pegRatio(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        pegRatio.place(x=2, y=380)

        deRatio = ctk.CTkLabel(self, 
                             text=stock.get_debtToEquity(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        deRatio.place(x=2, y=440)

        dividend = ctk.CTkLabel(self, 
                             text=stock.get_dividendPerShare(),
                             width=236,
                             height=20,
                             justify="center",
                             font=("Arial", 20),
                             text_color="#0ABAB5")
        dividend.place(x=2, y=500)




