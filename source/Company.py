def contains_number(value):
    if True in [char.isdigit() for char in value]:
        return True
    return False


def check_string(str: str):
    '''
    A function which checks the length of given str
    (should be at least 2 letters) and checks if the
    first letter is a capital letter.
    '''
    if contains_number(str):
        return False
    elif str[0].isupper() and len(str) >= 2:
        return True


def check_int(num: float):
    '''
    A function which returns True if the given number
    is positive and False otherwise
    '''
    if num <= 0:
        return False
    return True

class Company:
    # you can add methods for your usage

    def __init__(self, name: str, stocks_num: int,
                 stock_price: float, comp_type: str):
        if not check_string(name):
            raise ValueError("Error! Company name starts with capital letter.")
        else:
            self.name = name
        if not check_int(stocks_num):
            raise ValueError("Error! Number of stocks must be positive.")
        else:
            self.stocks_num = stocks_num
        if not check_int(stock_price):
            raise ValueError("Error! Price of stock must be positive.")
        else:
            self.stock_price = stock_price
        if not check_string(comp_type):
            raise ValueError("Error! Company type starts with capital letter.")
        else:
            self.comp_type = comp_type

    def net_worth(self):
        return self.stock_price*self.stocks_num

    def set_name(self, name):
        if name == self.name or check_string(name) == False:
            return False
        else:
            self.name = name
            return True

    def set_stocks_num(self, stocks_num):
        if not check_int(stocks_num):
            return False
        else:
            net_worth = self.net_worth()
            self.stocks_num = stocks_num
            self.stock_price = net_worth/self.stocks_num
            return True

    def set_stock_price(self, stock_price):
        if stock_price > self.net_worth() or check_int(stock_price) == False:
            return False
        else:
            net_worth = self.net_worth()
            self.stock_price = stock_price
            self.stocks_num = int(net_worth//self.stock_price)
            return True

    def set_comp_type(self, comp_type):
        if check_string(comp_type) == False:
            return False
        else:
            self.set_comp_type = comp_type
            return True

    def update_net_worth(self, net_worth):
        if check_int(net_worth) == False:
            return False
        else:
            self.set_stock_price = net_worth/self.set_stocks_num
            return True

    def add_stocks(self, number):
        new_stock_num = self.set_stocks_num + number
        if new_stock_num <= 0:
            return False
        else:
            self.set_stocks_num = new_stock_num
            return True

    def __str__(self):
        return f"{self.name}, {self.stocks_num} stocks, Price: {self.stock_price}, {self.comp_type}, Net Worth: {self.net_worth()}"

    def __repr__(self):
        return f"{self.name}, {self.stocks_num} stocks, Price: {self.stock_price}, {self.comp_type}, Net Worth: {self.net_worth()}"

    def __lt__(self, other):
        if self.net_worth() < other.net_worth():
            return True
        return False

    def __gt__(self, other):
        if self.net_worth() > other.net_worth():
            return True
        return False

    def __eq__(self, other):
        if self.net_worth() == other.net_worth():
            return True
        return False

    def __add__(self, other):
        new_company = Company(name=self.name,
                              stocks_num=self.stocks_num + other.stocks_num,
                              stock_price=(self.net_worth()+other.net_worth) /
                              (self.stocks_num + other.stocks_num),
                              comp_type=self.comp_type)
        return new_company
