# Company Class exercise

def contains_number(value: str):
    '''
    A function which checks if a value includes digits
    '''
    return any(map(str.isdigit, value))

def valid_name(str: str):
    '''
    A function which checks if the conditions of
    company name are met
    '''
    if str[0].isupper() is False or contains_number(str) or len(str) < 2:
        return False
    return True


class Company:
    # you can add methods for your usage

    # The constructor function
    def __init__(self, name: str, stocks_num: int,
                 stock_price: float, comp_type: str):
        if not valid_name(name):
            raise ValueError("Error! Company name starts with capital letter.")
        else:
            self.name = name
        if stocks_num < 0 or isinstance(stocks_num, int) is False:
            raise ValueError("Error! Number of stocks must be positive.")
        else:
            self.stocks_num = stocks_num
        if stock_price < 0:
            raise ValueError("Error! Price of stock must be positive.")
        else:
            self.stock_price = stock_price
        if not valid_name(comp_type):
            raise ValueError("Error! Company type starts with capital letter.")
        else:
            self.comp_type = comp_type

    def net_worth(self):
        '''
        Net worth of a company: as simple as that
        '''
        return self.stock_price*self.stocks_num

    def set_name(self, name):
        '''
        Updates the company name, as long as its valid
        '''
        if name == self.name or valid_name(name) is False:
            return False
        self.name = name
        return True

    def set_stocks_num(self, stocks_num):
        '''
        Updates the number of stocks, as long as its valid
        '''
        if stocks_num < 0 or isinstance(stocks_num, int) is False:
            return False
        net_worth = self.net_worth()
        self.stocks_num = stocks_num
        self.stock_price = net_worth/self.stocks_num
        return True

    def set_stock_price(self, stock_price):
        '''
        Updates the price of a stock, as long as its valid
        '''
        if stock_price > self.net_worth() or stock_price < 0:
            return False
        else:
            net_worth = self.net_worth()
            self.stock_price = stock_price
            self.stocks_num = int(net_worth/self.stock_price)
            return True

    def set_comp_type(self, comp_type):
        '''
        Updates the type of the copmany, as long as its valid
        '''
        if valid_name(comp_type):
            self.comp_type = comp_type
            return True
        return False

    def update_net_worth(self, net_worth):
        '''
        Updates the networth of the company
        '''
        if net_worth > 0:
            self.stock_price = net_worth / self.stocks_num
            return True
        return False

    def add_stocks(self, number):
        '''
        The function get int (numeber) and add it
        to the current number of stocks
        '''
        new_stock_num = self.stocks_num + number
        if isinstance(number, int) is False or new_stock_num <= 0:
            return False
        else:
            self.stocks_num = new_stock_num
            return True

    def __str__(self):
        '''
        A string with all the required data of the company
        '''
        return f"{self.name}, {self.stocks_num} stocks, Price: {self.stock_price}, {self.comp_type}, Net Worth: {self.net_worth()}"

    def __repr__(self):
        '''
        A string with all the required data of the company
        '''
        return f"{self.name}, {self.stocks_num} stocks, Price: {self.stock_price}, {self.comp_type}, Net Worth: {self.net_worth()}"

    def __lt__(self, other):
        '''
        Operator overloading - less than
        '''
        if self.net_worth() < other.net_worth():
            return True
        return False

    def __gt__(self, other):
        '''
        Operator overloading - greater than
        '''
        if self.net_worth() > other.net_worth():
            return True
        return False

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
        total_stocks = self.stocks_num + other.stocks_num
        new_company = Company(name=self.name,
                              stocks_num=self.stocks_num + other.stocks_num,
                              stock_price=(self.net_worth() + other.net_worth())/total_stocks,
                              comp_type=self.comp_type)
        return new_company
