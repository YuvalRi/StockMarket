from Company import Company, valid_name

# Stock Market Class exercise


def unique_name(lst: list):
    '''
    A function which checks if the elements
    in the list are unique
    '''
    return len(set(lst)) == len(lst)


class StockMarket:

    # The constructor function
    def __init__(self,
                 name: str,
                 min_net_worth_threshold: int,
                 stock_market_types: list,
                 companies=[]):
        if not valid_name(name):
            raise ValueError("Error! Please enter a valid name.")
        else:
            self.name = name
        if min_net_worth_threshold < 0:
            raise ValueError("Error! Please enter an unnegative number")
        else:
            self.min_net_worth_threshold = min_net_worth_threshold
        for ele in stock_market_types:
            if not valid_name(ele):
                raise ValueError("Error! Each element should be valid")
        else:
            self.stock_market_types = stock_market_types
        if not unique_name(companies):
            raise ValueError("Error! Each company has a unique name.")
        else:
            self.companies = []
            for j in range(len(companies)):
                for i in range(len(stock_market_types)):
                    if companies[j].comp_type in stock_market_types[i]:
                        self.companies.append(companies[j])

    def market_net_worth(self, comp_type: str):
        '''
        A function which returns the total net worth
        of all the companies of comp_type
        '''
        total = 0
        for comp in self.companies:
            if comp.comp_type == comp_type:
                total += comp.net_worth()
        return total

    def insert(self, c):
        '''
        A function adding a company (c) to the list
        of companies (companies)
        '''
        if c in self.companies or self.min_net_worth_threshold <= 0 or type(c) != Company:
            return False
        else:
            self.companies.append(c)
            return True

    def top_n(self, n: int):
        '''
        A function which returns net worth sorted list of
        the required companies from the biggest to the lowest
        '''
        if len(self.companies) == 0:
            return self.companies
        else:
            sorted_list = sorted(self.companies, reverse=True)
            if n > len(self.companies):
                return sorted_list
            return sorted_list[:n]

    def merger(self, c1, c2):
        '''
        A function which merges between 2 companies
        according to the required conditions
        '''
        if c1 in self.companies and c2 in self.companies:
            if c1 > c2 or c1 == c2:
                new_comp = c1 + c2
            else:
                new_comp = c2 + c1
            self.companies.append(new_comp)
            self.companies.clear(c1)
            self.companies.clear(c2)
        return None




















