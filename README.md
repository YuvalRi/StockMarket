# **Stock Market Project**

## Project summary
In this project I simulated stock market using two classes. The stock market class represents the entire set of companies that are found in the stock market and enables the user to conduct a variety of actions the different companies present in the market. By using the API given by the classes, different manipulations can be conducted such as changing net worth of companies, merging two companies and more. The company class represents a specific company and enables to edit parameters that charcterize the company. 

##  Project Design

### Company class
The company class is described using the following fields: 
* *name* - represents the name of the company. The type of this field is string. 
* *stocks_num* - represents the number of company's stocks. The type of this field is integer. 
* *stock_price* - represents the price of one stock. The type of this field is integer or float.
* *comp_type* - represents the type of the company. For example: High Tech, Pharmaceutical, Hardware, etc. The type of this field is string. 

The company class API includes the following functions:

* *net_worth* - calculates the company's net worth. 

* *set_name* - updates the name of the company

* *set_stocks_num* - updates the number of company's stocks. 

* *set_stocks_price* - updates the price of company's stock.

* *set_comp_type* - updates the company type.

* *update_net_worth* - updates the company's net worth such that number of stocks stay the same and the price of a stock changed. 

* *add_stocks* - addes a number to the current number of stocks. 

* *__repr__* - magic function which returns information about the company. 
For example: 
    
        "NVIDIA Corporation, 1000 stocks, 
         Price: 20.284, High Tech, Net Worth: 20284.0"

* *__lt__*, *__gt__*, *__eq__* - operator overloading: 

    lt = less than, gt = greate than, eq = equal to 

* *__add__* - operator overloading to the addition operator (+). This function merges two different companies to new one company. 

### StockMarket class
2. *StockMarket* - This class represents the whole stock market which contains a list of companies.

## Tests
In order to check the correctness of all the functions in both classes, I did a tests for each function by using 'pytest' testing tool.


