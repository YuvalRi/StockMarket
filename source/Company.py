
class Company:
    # you can add methods for your usage

    def __init__(self, name: str, stocks_num: int,
                 stock_price: int, comp_type: str):
        if not name[0].isupper or len(name) < 2:
            raise ValueError("Error! Company name starts with capital letter.")
        else:
            self.set_name = name
        if stocks_num <= 0:
            raise ValueError("Error! Number of stocks must be positive.")
        else:
            self.set_stocks_num = stocks_num
        if stock_price <= 0:
            raise ValueError("Error! Price of stock must be positive.")
        else:
            self.set_stock_price = stock_price
        if not comp_type[0].isupper or len(comp_type) < 2:
            raise ValueError("Error! Company type starts with capital letter.")
        else:
            self.set_comp_type = comp_type

    def net_worth(self):

        pass

    def set_name(self, name):

        pass

    def set_stocks_num(self, stocks_num):

        pass

    def set_stock_price(self, stock_price):

        pass

    def set_comp_type(self, comp_type):

        pass

    def update_net_worth(self, net_worth):

        pass

    def add_stocks(self, number):

        pass

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
