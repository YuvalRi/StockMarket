# **Stock Market Project**

## Project summary
In this project I simulated stock market using two classes. The stock market class represents the entire set of companies that are found in the stock market and enables the user to conduct a variety of actions the different companies present in the market. By using the API given by the classes, different manipulations can be conducted such as changing net worth of companies, merging two companies and more. The company class represents a specific company and enables to edit parameters that charcterize the company. 

##  Project Design

### Company class
The company class is described using the following fields: 
* **name** - represents the name of the company. The type of this field is string. 
* **stocks_num** - represents the number of company's stocks. The type of this field is integer. 
* **stock_price** - represents the price of one stock. The type of this field is integer or float.
* **comp_type** - represents the type of the company. For example: High Tech, Pharmaceutical, Hardware, etc. The type of this field is string. 

The company class API includes the following functions:

* *net_worth* - the function calculates the company's net worth. 

* *set_name* - the function receives a string and updates the name of the company accordingly. If an update occured, the function returns True. Otherwise, it will return False.

* *set_stocks_num* - the function receives the number of company's stocks and updates it accordingly. If an update occured, the function will return True. Otherwise, it will return False.

* *set_stocks_price* - the function receives the price of a stock and and updates it accordingly. If an update occured, the function will return True. Otherwise, it will return False.

* *set_comp_type* - the function receives the type of the company and updates it accordingly. If an update occured, the function will return True. Otherwise, it will return False.

* *update_net_worth* - the function receives net worth and update it such that number of stocks kept but the price of a stock change. If an update occured, the function will return True. Otherwise, it will return False.

* *add_stocks* - the function receives an integer and add it to the current number of stocks. 

* *__repr__* - the function returns the following string:
    
        "{NVIDIA Corporation}, {1000} stocks, 
         Price: {20.284}, {High Tech}, Net Worth: {20284.0}"

* *__lt__*, *__gt__*, *__eq__* - operator overloading that compares between two companies's net worth: 

    lt = less than, gt = greate than, eq = equal to 
for example:
for companies A and B with net worth of: 200.2 and 600.5 respectively, when calculating B > A, the function __gt__ returns True because the net work of B company is bigger than A net worth.

* *__add__* - operator overloading to the addition operator (+). This function recieves a company and merge it with the current company such that it will create a new company. 

### StockMarket class
The StockMarket class is described using the following fields: 
* **name** - represents the name of the stock market. The type of this field is string. 
* **min_net_worth_threshold** - represents the minimum threshold of company to be a part of the stock market. The type of this field is integer. 
* **stock_market_types** - represents the company types that can be a part of the stock market. The type of this field is a list of strings.
* **companies** - list with elements of company type. The list represents the different companies traded in the stock market.

The StockMarket class API includes the following functions:

* *market_net_worth* - the function recieves a company type and calculates the net worth of all the companies of comp type in the stock market. 

* *insert* - the function recieves a company (c) andd add it to the list of companies in the stock market.

* *top_n* - the function recieves an integer 'n' and returns sorted list of 'n' companies whose have the highest new worth. 

* *merger* - the function recieves two companies (c1 and c2) and merge between them.

## Tests
In order to check the correctness of all the functions in both classes, I did a tests for each function by using 'pytest' testing tool.

Examples:

```
c1 = Company("Google", 1000, 20.284, "High Tech")

# test net_worth method
def test_net_worth():
    assert c1.net_worth() == 20284.0


``` 
```
c5 = Company("Microsoft", 5000, 15.565, "High Tech")

# test insert method
def test_insert():
    assert stock_market.insert(c5) is True
    assert len(stock_market.companies) == 3
    assert stock_market.companies[2] == c5
```