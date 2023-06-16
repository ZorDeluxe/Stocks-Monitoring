"""
Description: Benjamin Graham model to calculate the
             intrinsic value of a stock. This is a
             helpful tool for defensive investor

Author: Zoren Dela Cruz
Created: 12-06-2023
"""
from stock import Stock
from Webscrapes.webscraper import Webscraping


class Lynch(Stock):
    """ Lynch Model Class """

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.name = name


    def evaluate(self) -> tuple:
        """ 
        Evaluation of the Lynch Model to determine if investing
        in the stock is profitable in the future

        Case: Less than 1 -> Overvalued
              Close to 1.5 -> Fairly Valued
              Close to 2 -> Under Valued
              Close to 3 -> Very Under Valued

        Returns:
            tuple: Peter Lynch Fair Value

        Yields:
            Iterator[tuple]: Fair Value, Comment
        """
        # Get key statistics
        g, pe, div = self.__key_statistics()
        try:
            fair_value = (g + div)/pe
        except ZeroDivisionError:   # PE is unidentified
            return 0, 'Invalid'

        if fair_value < 1.25:
            value = 'Overvalued'
        elif 1.25 <= fair_value < 1.75:
            value = 'Fairly Valued'
        elif  1.75 <= fair_value < 2.75:
            value = 'Under Valued'
        else:
            value = 'Very Under Valued'
        
        return fair_value, value


    def __key_statistics(self) -> tuple:
        """ Calculates the key information required
            to determine the Lynch Fair Value

        Returns:
            tuple: Key Statistics for Lynch Model

        Yields:
            Iterator[tuple]: Growth Rate, Price Earning Ratio, Dividend Yield
        """

        # Webscraping 
        url = f"https://nz.finance.yahoo.com/quote/{self.name}?p={self.name}&.tsrc=fin-srch"
        pe_ratio_css = "td[data-test=PE_RATIO-value]"
        div_yield_css = "td[data-test=DIVIDEND_AND_YIELD-value]"

        web = Webscraping()

        # Price to Earning Ratio
        try:
            result = web.extract_value(url, pe_ratio_css)
            pe_ratio = float(result)
        except ValueError:
            pe_ratio = 0

        # Dividend Yield
        try:
            result = web.extract_value(url, div_yield_css).split(" ")[-1]
            div_yield = float(result.removesuffix('%)').removeprefix('('))
        except ValueError:
            div_yield = 0

        # Earnings per share
        growth_rate = self.get_growthRate()

        return growth_rate, pe_ratio, div_yield


        

