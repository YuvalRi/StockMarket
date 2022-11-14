from Company import Company
from StockMarket import StockMarket

# creating the required classes 
c1 = Company("Google", 1000, 20.284, "High Tech")
c2 = Company("Lenovo", 1000, 5, "High Tech")
c3 = Company("Pfizer", 4000, 10, "Pharmaceutical")
c4 = Company("Apple", 5000, 10.4, "Hardware")

stock_market = StockMarket("Nasdaq", 
                            6000,
                            ["High Tech", "Hardware"],
                            companies=[c1, c2, c3, c4])

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
