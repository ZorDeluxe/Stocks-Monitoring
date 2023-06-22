import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import threading

from Stocks.Quantitive.Benjamin import Benjamin
from Stocks.Quantitive.DCF import DCF
from Stocks.Quantitive.Lynch import Lynch

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper

class AnalysisFrame(ctk.CTkFrame):
    """ Creates the Statistics Preview of Stocks """

    def __init__(self, parent, stock_name):
        super().__init__(parent, 
                         height=100, 
                         width=800)
        self.place(x=0, y=700)

        self.__Benjamin_Model(stock_name)
        self.__DCF_Model(stock_name)
        self.__Lynch_Model(stock_name)
        self.__placeholder(stock_name)

    @threaded
    def __Benjamin_Model(self, stock_name):

        benjamin = Benjamin(stock_name)
        buy, value = benjamin.evaluate() 

        bjFrame = ctk.CTkFrame(self, 
                               height=100, 
                               width=196,
                               border_width=2)
        bjFrame.place(x=0, y=0)

        benjaminLabel = ctk.CTkLabel(bjFrame, 
                                     text="Graham Model",
                                     width=75,
                                     height=15,
                                     font=('Arial', 12))
        benjaminLabel.place(y=5, relwidth=1)

        intLabel = ctk.CTkLabel(bjFrame, 
                                text="Intrinsic Value",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        intLabel.place(y=25, relwidth=1)

        valueLabel = ctk.CTkLabel(bjFrame, 
                             text=f'${value}',
                             width=236,
                             height=15,
                             justify="center",
                             font=("Arial", 12),
                             text_color="#0ABAB5")
        valueLabel.place(y=40, relwidth=1)

        div = ttk.Separator(bjFrame, 
                                orient="horizontal")
        div.place(x=49, y=60, relwidth=0.5)

        buyingLabel = ctk.CTkLabel(bjFrame, 
                                text="Buy",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        buyingLabel.place(y=65, relwidth=1)

        buyLabel = ctk.CTkLabel(bjFrame, 
                             text=f'{buy}',
                             width=236,
                             height=15,
                             justify="center",
                             font=("Arial", 12),
                             text_color="#0ABAB5")
        buyLabel.place(y=80, relwidth=1)

    @threaded
    def __DCF_Model(self, stock_name):
        dcf = DCF(stock_name)
        buy, value = dcf.evaluate() 

        dcfFrame = ctk.CTkFrame(self, 
                               height=100, 
                               width=196,
                               border_width=2)
        dcfFrame.place(x=200, y=0)

        heading = ctk.CTkLabel(dcfFrame, 
                                text="DCF Model",
                                width=75,
                                height=15,
                                font=('Arial', 12))
        heading.place(y=5, relwidth=1)

        intLabel = ctk.CTkLabel(dcfFrame, 
                                text="Intrinsic Value",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        intLabel.place(y=25, relwidth=1)

        valueLabel = ctk.CTkLabel(dcfFrame, 
                             text=f'${value}',
                             width=236,
                             height=15,
                             justify="center",
                             font=("Arial", 12),
                             text_color="#0ABAB5")
        valueLabel.place(y=40, relwidth=1)

        div = ttk.Separator(dcfFrame, 
                                orient="horizontal")
        div.place(x=49, y=60, relwidth=0.5)

        buyingLabel = ctk.CTkLabel(dcfFrame, 
                                text="Buy",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        buyingLabel.place(y=65, relwidth=1)

        buyLabel = ctk.CTkLabel(dcfFrame, 
                             text=f'{buy}',
                             width=236,
                             height=15,
                             justify="center",
                             font=("Arial", 12),
                             text_color="#0ABAB5")
        buyLabel.place(y=80, relwidth=1)

    @threaded
    def __Lynch_Model(self, stock_name):
        lynch = Lynch(stock_name)
        fair_value, value = lynch.evaluate() 

        dcfFrame = ctk.CTkFrame(self, 
                            height=100, 
                            width=196,
                            border_width=2)
        dcfFrame.place(x=400, y=0)

        heading = ctk.CTkLabel(dcfFrame, 
                                text="Lynch Model",
                                width=75,
                                height=15,
                                font=('Arial', 12))
        heading.place(y=5, relwidth=1)

        intLabel = ctk.CTkLabel(dcfFrame, 
                                text="Fair Value",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        intLabel.place(y=25, relwidth=1)

        valueLabel = ctk.CTkLabel(dcfFrame, 
                            text=f'{fair_value}',
                            width=236,
                            height=15,
                            justify="center",
                            font=("Arial", 12),
                            text_color="#0ABAB5")
        valueLabel.place(y=40, relwidth=1)

        div = ttk.Separator(dcfFrame, 
                                orient="horizontal")
        div.place(x=49, y=60, relwidth=0.5)

        buyingLabel = ctk.CTkLabel(dcfFrame, 
                                text="Buy",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        buyingLabel.place(y=65, relwidth=1)

        buyLabel = ctk.CTkLabel(dcfFrame, 
                            text=f'{value}',
                            width=236,
                            height=15,
                            justify="center",
                            font=("Arial", 12),
                            text_color="#0ABAB5")
        buyLabel.place(y=80, relwidth=1)

    def __placeholder(self, stock_name):
        dcfFrame = ctk.CTkFrame(self, 
                               height=100, 
                               width=196,
                               border_width=2)
        dcfFrame.place(x=600, y=0)

        heading = ctk.CTkLabel(dcfFrame, 
                                text="Unknown Model",
                                width=75,
                                height=15,
                                font=('Arial', 12))
        heading.place(y=5, relwidth=1)

        intLabel = ctk.CTkLabel(dcfFrame, 
                                text="Intrinsic Value",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        intLabel.place(y=25, relwidth=1)

        valueLabel = ctk.CTkLabel(dcfFrame, 
                             text=f'$0.00',
                             width=236,
                             height=15,
                             justify="center",
                             font=("Arial", 12),
                             text_color="#0ABAB5")
        valueLabel.place(y=40, relwidth=1)

        div = ttk.Separator(dcfFrame, 
                                orient="horizontal")
        div.place(x=49, y=60, relwidth=0.5)

        buyingLabel = ctk.CTkLabel(dcfFrame, 
                                text="Buy",
                                width=75,
                                height=15,
                                font=('Arial', 10))
        buyingLabel.place(y=65, relwidth=1)

        buyLabel = ctk.CTkLabel(dcfFrame, 
                             text=f'Unknown',
                             width=236,
                             height=15,
                             justify="center",
                             font=("Arial", 12),
                             text_color="#0ABAB5")
        buyLabel.place(y=80, relwidth=1)

   