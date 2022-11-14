from Company import Company
from StockMarket import StockMarket

def main():
    print("#################Company tests#################")
    print("1. create Company instance:")
    c1 = Company("Google", 1000, 20.284, "High Tech")
    print(c1)
    print("2. test net_worth method:")
    print(c1.net_worth())
    print("3. test set_name method:")
    print(c1.set_name("Google2"))
    print(c1.set_name("Google Two"))
    print(c1)
    print("4. test set_stocks_num method:")
    print(c1.set_stocks_num(2000))
    print(c1)
    print("5. test set_stock_price method:")
    print(c1.set_stock_price(25))
    print(c1)
    print("6. test set_comp_type method:")
    print(c1.set_comp_type("General"))
    print(c1)
    print("7. test update_net_worth method:")
    print(c1.update_net_worth(0))
    print(c1)
    print(c1.update_net_worth(2027.5))
    print(c1)
    print("8. test add_stocks method:")
    print(c1.add_stocks(-850))
    print(c1)
    print(c1.add_stocks(8000))
    print(c1)
    print("9. test Operator Overloading:")
    c2 = Company("Lenovo", 1000, 5, "High Tech")
    print(c2)
    print(c1 > c2)
    print(c1 < c2)
    print(c1 == c2)
    print(c1 + c2)

    print("#################StockMarket tests#################")
    c1 = Company("Google", 1000, 20.284, "High Tech")
    c2 = Company("Lenovo", 1000, 5, "High Tech")
    c3 = Company("Pfizer", 4000, 10, "Pharmaceutical")
    c4 = Company("Apple", 5000, 10.4, "Hardware")

    print("1. create StockMarket instance:")
    stock_market = StockMarket("Nasdaq", 6000, ["High Tech", 
                               "Hardware"], companies=[c1, c2, c3, c4])
    for company in stock_market.companies:
        print(company)

    print("2. test insert method:")
    c5 = Company("Microsoft", 5000, 15.565, "High Tech")
    print(stock_market.insert(c5))
    for company in stock_market.companies:
        print(company)

    print("3. test market_net_worth method:")
    print(stock_market.market_net_worth("High Tech"))
    print(stock_market.market_net_worth("Pharmaceutical"))

    print("4. test top_n method:")
    top_n_companies = stock_market.top_n(2)
    for company in top_n_companies:
        print(company)

    print("5. test merger method:")
    new_c = stock_market.merger(c4, c5)
    print(new_c)
    for company in stock_market.companies:
        print(company)

if __name__ == "__main__":
    main()

