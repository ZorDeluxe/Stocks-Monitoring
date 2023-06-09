"""
Description: Stock Class encapsulates information needed
             about the stock. All information is taken from
             yahoo finance and other supporting websites


    Author:  Zoren Dela Cruz
    Modified: 07/06/2023
"""
import yahoo_fin.stock_info as yn
import yfinance as yf
import yahooquery as yq

from pandas import DataFrame

class Stock:
    """ The Stock Class """


    def __init__(self, name: str) -> None:
        """
        Constructor for the stock class

        Args:
            name (str): Name of the stock
        """
        self.name = name

        # Creates a Ticker for Yahoo finance
        self.yf_stock = yf.Ticker(self.name)
        self.yq_stock = yq.Ticker(self.name)


    def get_currentPrice(self) -> float:
        """ Returns the current value of the stock

        Returns:
            float: Stock's current value
        """
        self.currentPrice = self.info['currentPrice']
        return self.currentPrice


    def get_EPS(self) -> float:
        """ Returns the Earnings Per Share of the stock

        Returns:
            float: Earnings Per Share
        """
        self.eps = self.info['trailingEps']
        return self.eps
    

    def get_growthRate(self) -> float:
        """ Returns the Growth Rate for next 5 years

        Returns:
            float: Growth Rate for next 5 years
        """
        self.yn_stock = yn.get_analysts_info(self.name)

        # In Growth Estimate Table, Column 4 gives growth rate in 5 years
        growth_str = self.yn_stock['Growth Estimates'][self.name][4]
        growth_str = growth_str.removesuffix('%')
        self.growthRate = float(growth_str)
        
        return self.growthRate


    def get_dividends(self) -> DataFrame:
        """ Gives a Dividend History of the Stock

        Returns:
            DataFrame: Dividend History 
        """
        return yn.get_dividends(self.name)


    def get_cash_flow(self, frequency="a") -> DataFrame:
        """ Gives a Cash Flow History of the Stock

        Args:
            frequency (str, optional): Defaults to "a" for Annual.
                                       Type "q" for Quarterly

        Returns:
            DataFrame: Cash Flow History
        """
        return self.yq_stock.cash_flow(frequency)
    

    def get_balance_sheet(self, frequency="a") -> DataFrame:
        """ Gives the Balance Sheet of the Stock

        Args:
            frequency (str, optional): Defaults to "a" for Annual.
                                       Type "q" for Quarterly

        Returns:
            DataFrame: Balance Sheet History
        """
        return self.yq_stock.balance_sheet(frequency)
    

    def get_income_statement(self, frequency="a") -> DataFrame:
        """ Gives the Income Statement of the Stock

        Args:
            frequency (str, optional): Defaults to "a" for Annual.
                                       Type "q" for Quarterly

        Returns:
            DataFrame: Income Statement History
        """
        return self.yq_stock.income_statement(frequency)
    
