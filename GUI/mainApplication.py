import tkinter as tk
import customtkinter as ctk

from Frames.chartFrame import ChartFrame
from Frames.selectFrame import SelectFrame

ctk.set_appearance_mode("light")


class MainApplication(ctk.CTk):
    """ Main Frame of the stocks application """

    def __init__(self, *args, **kwargs):
        """ Creates an instance of the GUI """

        # Core Setup
        super().__init__()
        self.title("Stocks Monitor")
        self.geometry('800x600')
        self.resizable(False, False)        # Application not resizable

        # Create Frames
        self.selectFrame = SelectFrame(self)
        self.chartFrame = ChartFrame(self)

        # Continous Loop
        self.mainloop()
        
if __name__ == "__main__":
    MainApplication()