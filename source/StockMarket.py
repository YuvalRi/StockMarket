from Company import Company
from Company import valid_name

# Stock Market Class exercise


def unique_name(lst: list):
    '''
    A function which checks if the strings
    in the list are unique
    '''
    if len(set(lst)) == len(lst):
        return True
    return False


class StockMarket:

    # The constructor function
    def __init__(self,
                 name: str,
                 min_net_worth_threshold: int,
                 stock_market_types: list,
                 companies=[]):
        if not valid_name(name):
            raise ValueError("Error! Please enter a valid name.")
        if min_net_worth_threshold < 0:
            raise ValueError("Error! Please enter an unnegative number")
        for ele in stock_market_types:
            if not valid_name(ele):
                raise ValueError("Error! Each element should be valid")
        if not unique_name(companies):
            raise ValueError("Error! Each company has a unique name.")
    
    def market_net_worth(self, comp_type: str):
        if StockMarket.



