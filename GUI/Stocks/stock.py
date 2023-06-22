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
        self.currentPrice = self.yq_stock.financial_data[self.name]['currentPrice']
        return self.currentPrice


    def get_EPS(self) -> float:
        """ Returns the Earnings Per Share of the stock

        Returns:
            float: Earnings Per Share
        """
        self.eps = self.yq_stock.key_stats[self.name]['trailingEps']
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
    
    
    def get_sharesOutstanding(self) -> float:
        """ Returns the stocks shares oustanding

        Returns:
            float: Shares outstanding
        """
        self.sharesOustanding = self.yq_stock.key_stats[self.name]['sharesOutstanding']
        return self.sharesOustanding
    
    
    def get_priceToEarning(self) -> float:
        """ Returns the price to earning ratio

        Returns:
            float: Price to Earning Ratio
        """
        self.peRatio = self.yq_stock.key_stats[self.name]['forwardPE']
        return round(self.peRatio, 2)
    

    def get_priceToBook(self) -> float:
        """ Returns the stocks price to book ratio

        Returns:
            float: P/B Ratio
        """
        self.pbRatio = self.yq_stock.key_stats[self.name]['priceToBook']
        return round(self.pbRatio, 2)       # Round the value by 2dp for display


    def get_pegRatio(self) -> float:
        """ Returns the stock's PEG ratio

        Returns:
            float: PEG Ratio
        """
        self.pegRatio = self.yq_stock.key_stats[self.name]['pegRatio']
        return self.pegRatio
    

    def get_debtToEquity(self) -> float:
        """ Returns the Debt to Equity Ratio

        Returns:
            float: Debt to Equity Ratio
        """
        self.deRatio = self.yq_stock.financial_data[self.name]['debtToEquity']
        return round(self.deRatio, 2)


    def get_dividends(self) -> DataFrame:
        """ Gives a Dividend History of the Stock

        Returns:
            DataFrame: Dividend History 
        """
        return yn.get_dividends(self.name)
    

    def get_dividendPerShare(self) -> float:
        try:
            divdends = yn.get_dividends(self.name)
            return float(divdends['dividend'][-1])             # Latest Dividend per share
        except:
            return 0.0


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
    

    def get_price_history(self, period: str='2y') -> DataFrame:
        """ Gives the historical price data

        Args:
            period (str, optional): Period options = 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max. 
                                    Defaults to '2y'.

        Returns:
            DataFrame: Stock historical price data
        """
        return self.yf_stock.history(period)['Close']
    
if __name__ == "__main__":
    msft = Stock('MSFT')
    print(msft.yq_stock.recommendation_trend)