import tkinter as tk
import customtkinter as ctk

class StatsFrame(ctk.CTkFrame):
    """ Creates the Statistics Preview of Stocks """

    def __init__(self, parent):
        super().__init__(parent, fg_color = 'red', height=600, width=240)
        self.place(x=0, y=100)


