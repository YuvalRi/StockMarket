def check_string(str: str):
    '''
    A function which checks the length of given str
    (should be at least 2 letters) and checks if the
    first letter is a capital letter.
    '''
    if not str[0].isupper() or len(str) >= 2:
        return False
    return True


def check_int(num: int):
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
                 stock_price: int, comp_type: str):
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
        if not check_string(name) or self.name == name:
            return False
        else:
            name = self.name
            return True

    def set_stocks_num(self, stocks_num):
        if not stocks_num != self.stocks_num or check_int(stocks_num):
            return False
        else:
            stocks_num = self.stocks_num
            return True

    def set_stock_price(self, stock_price):
        if not check_int(stock_price) or stock_price < self.net_worth():
            return False
        else:
            stock_price == self.stock_price
            return True

    def set_comp_type(self, comp_type):
        if not check_string(comp_type) or comp_type == self.comp_type:
            return False
        else:
            comp_type = self.set_comp_type
        return True

    def update_net_worth(self, net_worth):
        if not check_int(net_worth) or net_worth != self.net_worth():
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

    def __repr__(self):

        pass

    def __lt__(self, other):

        pass

    def __gt__(self, other):

        pass

    def __eq__(self, other):

        pass

    def __add__(self, other):
        pass
