# Stock Market Class exercise

def contains_number(value):
    '''
    A function which checks if a value includes digits
    '''
    if True in [char.isdigit() for char in value]:
        return True
    return False


def valid_name(str: str):
    '''
    A function which checks if the conditions of
    company name are met
    '''
    if str[0].isupper() is False or contains_number(str) or len(str) < 2:
        return False
    return True


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
