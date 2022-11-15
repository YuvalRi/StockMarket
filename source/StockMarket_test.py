from Company import Company
from StockMarket import StockMarket

""" StockMarket Tests """

# creating the required classes 
c1 = Company("Google", 1000, 20.284, "High Tech")
c2 = Company("Lenovo", 1000, 5, "High Tech")
c3 = Company("Pfizer", 4000, 10, "Pharmaceutical")
c4 = Company("Apple", 5000, 10.4, "Hardware")

# creating stock market
stock_market = StockMarket("Nasdaq", 
                            6000,
                            ["High Tech", "Hardware"],
                            companies=[c1, c2, c3, c4])

# test creation of StockMarket instance
def test_stockmarket_instance():
    assert len(stock_market.companies) == 2
    assert stock_market.companies[0] == c1
    assert stock_market.companies[1] == c4

# create new company
c5 = Company("Microsoft", 5000, 15.565, "High Tech")

# test insert method
def test_insert():
    assert stock_market.insert(c5) == True
    assert len(stock_market.companies) == 3
    assert stock_market.companies[2] == c5

# test market net worth method:

def test_net_worth1():
    assert stock_market.market_net_worth("High Tech") == 98109.0
    assert stock_market.market_net_worth("Pharmaceutical") == 0

# test top_n method:
def test_top_n():
    top_n_companies = stock_market.top_n(2)
    assert top_n_companies[0] == c5
    assert top_n_companies[1] == c4

# create new company
c6 = Company("Microsoft", 10000, 12.9825, "High Tech")

# test merger method:
def test_merger():
    assert len(stock_market.companies) == 3
    new_comp = stock_market.merger(c4, c5)
    assert new_comp is not None
    assert new_comp == c6
    assert stock_market.companies[0] == c1
    assert stock_market.companies[1] == c6

