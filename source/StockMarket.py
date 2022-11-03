from Company import valid_name
# Stock Market Class exercise


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
            raise ValueError("Error! Please enter unnegative number.")
        



                


    
    
