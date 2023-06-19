"""
Description: Benjamin Graham model to calculate the
             intrinsic value of a stock. This is a
             helpful tool for defensive investor

Author: Zoren Dela Cruz
Created: 06-06-2023
"""
import sys
import os

# Importing modules 
script_dir = os.path.dirname(__file__)
webscrapes_dir = os.path.join(script_dir, '..', '..', 'Webscrapes')
sys.path.append(webscrapes_dir)

from stock import Stock
from Helper.webscraper import Webscraping


class Benjamin(Stock):
    """ Benjamin Graham Model Class """

    AAA_yield = None

    def __init__(self, stock: str, conservative: bool = True) -> None:
        """ Initialising the attributes for Benjamin Graham Model """
        super().__init__(stock)

        # Get Corporate Yield 
        if not Benjamin.AAA_yield:
            Benjamin.AAA_yield = self.__get_corporate_yield()

        # Benjamin Model
        self.stock = stock
        self.conservative = conservative

        # Get Key Statistic for Benjamin Model
        self.__keyStatistics()


    def evaluate(self, MOS: float=35) -> bool:
        """
        Evaluation of the Benjamin Model to determine if investing
        in the stock is profitable in the future

        Args:
            MOS (float): Margin of Safety (Default = 35%)

        Returns:
            bool: Suggest user to invest in the stock
        """
        # Calculates the Intrinisc Value
        self.get_intrinsic_value()

        # Convert MOS into decimal
        percentage_MOS = 1 - (MOS / 100)

        # Acceptable Buy Price
        self.accept_buy_price = self.intrinsic_value * percentage_MOS

        # Determine if stock should be bought
        if self.accept_buy_price > self.currentPrice:
            return True
        else:
            return False


    def get_intrinsic_value(self) -> float:
        """
        Caclulates the Intrinsic Value of the stock
        given the conservative status

        Returns:
            float: Stock's Intrinisic Value
        """
        # Conservative Model V = [EPS x (7 + g) x 4.4] / Y
        if self.conservative:
            self.intrinsic_value = (
                self.eps * (7.0 + self.growthRate) * 4.4) / self.AAA_yield
        else:  # V = [EPS x (8.5 + 2g) x 4.4] / Y
            self.intrinsic_value = (
                self.eps * (8.5 + (2 * self.growthRate)) * 4.4) / self.AAA_yield
        return self.intrinsic_value


    def __get_corporate_yield(cls) -> float:
        """
        Uses Selenium to Webscrape the latest AAA yield

        Returns:
            float: AAA Corporate Yield
        """
        # Webscrape the AAA corporate yield
        url = 'https://fred.stlouisfed.org/series/AAA'
        css_element = 'span[class="series-meta-observation-value"]'

        web = Webscraping()
        values = web.extract_values(url, css_element)

        # The end of the list gives corporate yield       
        return float(values[-1])
    

    def __keyStatistics(self) -> None:
        """
        Scrapes the key statistic needed to calculate 
        for the Benjamin Model
        """
        self.get_currentPrice()
        self.get_growthRate()
        self.get_EPS()

    

