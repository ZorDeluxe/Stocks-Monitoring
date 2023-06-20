import tkinter as tk
import customtkinter as ctk

class SelectFrame(ctk.CTkFrame):
    """ Select Frame to choose what stock to display """

    def __init__(self, parent):
        """ Instatiate the select Frame """
        super().__init__(parent, height=100, width=800, fg_color="white")
        self.place(x=0, y=0)

        # frameLabel = ctk.CTkLabel(self, text="Select", width=50, height=20, font=('Arial', 15))
        # frameLabel.place(x=10, y=10)

        # stockEntry = ctk.CTkEntry(self, placeholder_text='Search', width=150, height=20, font=('Arial', 12))
        # stockEntry.place(x=50, y=35)


        