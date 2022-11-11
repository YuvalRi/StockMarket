# Company Class exercise

def contains_number(value: str):
    '''
    A function which checks if a value includes digits
    '''
    if any(map(str.isdigit, value)):
        return True
    else:
        return False


def valid_name(str: str):
    '''
    A function which checks if the conditions of
    company name are met
    '''
    if str[0].isupper() is False or contains_number(str) or len(str) < 2:
        return False
    elif str[0].isupper() and len(str) >= 2 and str[1:].isupper() is False:
        return True


def check_int(val):
    '''
    A function which checks if a given number is int
    '''
    return isinstance(val, int)


class Company:
    # you can add methods for your usage

    # The constructor function
    def __init__(self, name: str, stocks_num: int,
                 stock_price: float, comp_type: str):
        pass

    def net_worth(self):
        '''
        Net worth of a company: as simple as that
        '''
        pass

    def set_name(self, name):
        '''
        Updates the company name, as long as its valid
        '''
        pass

    def set_stocks_num(self, stocks_num):
        '''
        Updates the number of stocks, as long as its valid
        '''
        pass

    def set_stock_price(self, stock_price):
        '''
        Updates the price of a stock, as long as its valid
        '''
        pass

    def set_comp_type(self, comp_type):
        '''
        Updates the type of the copmany, as long as its valid
        '''
        pass

    def update_net_worth(self, net_worth):
        '''
        Updates the networth of the company
        '''
        pass

    def add_stocks(self, number):
        '''
        The function get int (numeber) and add it
        to the current number of stocks
        '''
        pass

    def __str__(self):
        '''
        A string with all the required data of the company
        '''
        pass

    def __repr__(self):
        '''
        A string with all the required data of the company
        '''
        pass

    def __lt__(self, other):
        '''
        Operator overloading - less than
        '''
        pass

    def __gt__(self, other):
        '''
        Operator overloading - greater than
        '''
        pass

    def __eq__(self, other):
        '''
        Operator overloading - equal to
        '''
        if self.net_worth() == other.net_worth():
            return True
        return False

    def __add__(self, other):
        '''
        Operator overloading which merges two companies into one
        '''
        pass
