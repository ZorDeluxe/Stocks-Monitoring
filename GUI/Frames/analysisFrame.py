import tkinter as tk
import customtkinter as ctk

class AnalysisFrame(ctk.CTkFrame):
    """ Creates the Statistics Preview of Stocks """

    def __init__(self, parent):
        super().__init__(parent, height=100, width=800, fg_color='blue')
        self.place(x=0, y=700)