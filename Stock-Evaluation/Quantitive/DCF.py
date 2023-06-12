"""
Description: Benjamin Graham model to calculate the
             intrinsic value of a stock. This is a
             helpful tool for defensive investor

Author: Zoren Dela Cruz
Created: 06-06-2023
"""
from stock import Stock

class DCF(Stock):
    """ Discount Cash Flow Class """

    def __init__(self, name: str) -> None:
        """ Constructor for DCF Analysis

        Args:
            name (str): Name of the stock
        """
        super().__init__(name)


    def evaluate(self, MOS=35) -> bool: 
        """
        Evaluation of the DCF Model to determine if investing
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
        if self.accept_buy_price > self.get_currentPrice():
            return True
        else:
            return False


    def get_intrinsic_value(self) -> float:
        """ Calculates the Intrinsic Value of Stock

        Returns:
            float: DCF Price Per Share
        """
        balance_sheet = self.get_balance_sheet()
        # Key Statistics
        sum_pv_ffcf = self.__get_PV_FCFF()
        cash_equivalent = balance_sheet['CashAndCashEquivalents'][-1]
        total_debt =  balance_sheet['TotalDebt'][-1]
        equity_value = sum_pv_ffcf + cash_equivalent - total_debt
        shares_oustanding = self.get_sharesOutstanding() 

        # Comparison
        self.intrinsic_value = equity_value / shares_oustanding
        return self.intrinsic_value


    def __get_average_growth_rate(self) -> float:
        """ Calculates the average growth rate in 5 year span

        Returns:
            float: Average growth rate
        """
        free_cashflow = self.get_cash_flow()['FreeCashFlow'][:-2]
        print(free_cashflow)
        total_growth_rate = 0

        for i in range(1, len(free_cashflow)):
            growth_rate = (free_cashflow[i] - free_cashflow[i-1]) / free_cashflow[i]
            print(growth_rate)
            total_growth_rate += growth_rate
            
            
        average_growth_rate = total_growth_rate / len(free_cashflow)
        print(average_growth_rate)

        return average_growth_rate
    

    def __get_PV_FCFF(self) -> float:
        """ Calculates the present value of future cash flow

        Returns:
            float: Sum of the Present Value of Future Cash Flow
        """
        # Fixed Values
        perp_growth_rate = 0.025     # Perpetual Growth Rate
        discount_rate = 0.08         # Discount Rate 

        # Dynamic Values
        recent_cash_flow = self.get_cash_flow()['FreeCashFlow'][-1]
        avg_growth_rate = self.__get_average_growth_rate()

        # Predicting the cash flow for next 10 years
        future_cash_flow_list = []
        pv_ffcf_list = []
        sum_pv_ffcf = 0
        for i in range(10):

            if i == 9:         # Calculate Terminal Value
                terminal_value = (future_cash_flow_list[-1] * (1 + perp_growth_rate)) / (perp_growth_rate + discount_rate)
                future_cash_flow_list.append(terminal_value)
            else:
                predict_cash_flow = recent_cash_flow * (1 + avg_growth_rate)
                future_cash_flow_list.append(predict_cash_flow)


        for i in range(len(future_cash_flow_list)):
            pv_cash_flow = predict_cash_flow / ((1+discount_rate) ** (i+1))
            pv_ffcf_list.append(pv_cash_flow)
            sum_pv_ffcf += pv_cash_flow

        print(sum_pv_ffcf)

        return sum_pv_ffcf




        



