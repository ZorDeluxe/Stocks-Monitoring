import tkinter as tk

import customtkinter as ctk
import threading

from Frames.analysisFrame import AnalysisFrame
from Frames.chartFrame import ChartFrame
from Frames.statisticsFrame import StatsFrame

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper


class SelectFrame(ctk.CTkFrame):
    """ Select Frame to choose what stock to display """
    stocks_list = {'TSLA'}
    stock_name = 'TSLA'
    stock_wanted = 'TSLA'

    def __init__(self, parent, chart: ChartFrame, analysis: AnalysisFrame, stats: StatsFrame):
        """ Instatiate the select Frame """
        super().__init__(parent, height=100, width=800)
        self.place(x=0, y=0)

        # Frames to update
        self.chart = chart
        self.analysis = analysis
        self.stats = stats

        ####################################################
        #                   Search Frame                   #
        ####################################################
        searchFrame = ctk.CTkFrame(self,
                                   width=398,
                                   height=100,
                                   border_width=2)
        searchFrame.place(x=0, y=0)

        frameLabel = ctk.CTkLabel(searchFrame,
                                  text="Search",
                                  width=50,
                                  height=20,
                                  font=('Arial', 15))
        frameLabel.place(x=10, y=10)

        self.stockEntry = ctk.CTkEntry(searchFrame,
                                       width=150,
                                       height=35,
                                       placeholder_text='Search',
                                       font=('Arial', 12))
        self.stockEntry.place(x=50, y=45)

        self.searchButton = ctk.CTkButton(searchFrame,
                                     text='Search',
                                     width=75,
                                     height=35,
                                     hover_color='#bec7d4',
                                     command=lambda: self.__search_button_event(event=0))
        self.searchButton.place(x=210, y=45)

        searchAddButton = ctk.CTkButton(searchFrame,
                                        text='Add',
                                        width=75,
                                        height=35,
                                        hover_color='#bec7d4',
                                        command=self.__add_button_event)
        searchAddButton.place(x=290, y=45)

        ####################################################
        #                    Menu Frame                    #
        ####################################################
        self.menuFrame = ctk.CTkFrame(self,
                                      width=398,
                                      height=100,
                                      border_width=2)
        self.menuFrame.place(x=400, y=0)

        menuLabel = ctk.CTkLabel(self.menuFrame,
                                 text='Shortcut',
                                 width=75,
                                 height=20,
                                 font=('Arial', 15), 
                                 justify='left')
        menuLabel.place(x=10, y=10)

        self.stockMenu_var = ctk.StringVar(value=list(self.stocks_list)[0])
        self.optionMenu = ctk.CTkOptionMenu(self.menuFrame,
                                            width=150,
                                            height=35,
                                            values=list(self.stocks_list),
                                            command=self.__get_stock_option_selection,
                                            variable=self.stockMenu_var)
        self.optionMenu.place(x=50, y=45)

        self.menuSearchButton = ctk.CTkButton(self.menuFrame,
                                         text='Search',
                                         width=75,
                                         height=35,
                                         hover_color='#bec7d4',
                                         command=lambda: self.__search_button_event(event=1))
        self.menuSearchButton.place(x=210, y=45)

    def __get_stock_option_selection(self, selection: str) -> None:
        """ Gets the stock option selected

        Args:
            selection (str): Selected Stock from Option Menu
        """
        self.stock_wanted = selection

    def __add_button_event(self):
        """
        Adds the stock of interest into option menu
        """
        stock_name = self.stockEntry.get()
        self.stocks_list.add(stock_name)
        self.optionMenu.configure(values=self.stocks_list)

    @threaded
    def __search_button_event(self, event: int) -> None:
        """ Updates the stock name depending on the frame

        Args:
            event (int): From search frame, int = 0
                         From select frame, int = 1
        """
        if (event == 0):
            self.stock_name = self.stockEntry.get()
        else:
            self.stock_name = self.stock_wanted

        # Update frames
        self.searchButton.configure(state='disabled')
        self.menuSearchButton.configure(state='disabled')


        chartThread = threading.Thread(target=self.chart.updateCharts, args=(self.stock_name,))
        analysisThread = threading.Thread(target=self.analysis.update_analysis_frame, args=(self.stock_name,))
        statsThread = threading.Thread(target=self.stats.update_stats_frame, args=(self.stock_name,))

        chartThread.start()
        analysisThread.start()
        statsThread.start()

        chartThread.join()
        analysisThread.join()
        statsThread.join()
        
        self.searchButton.configure(state='normal')
        self.menuSearchButton.configure(state='normal')

        
