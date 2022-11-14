from Company import Company

""" Company Tests """

# create Company instance
c1 = Company("Google", 1000, 20.284, "High Tech")
 
 # test net_worth method 
def test_net_worth():
    net_worth = c1.net_worth()
    assert net_worth == 20284.0

# test set_name method 
def test_set_name_1():
    test_name = c1.set_name("Google2")
    assert test_name == False

def test_set_name_2():
    test_name = c1.set_name("Google Two")
    assert test_name == True

# test set_stocks_num method
def test_set_stocks_num():
    test_stocks_num = c1.set_stocks_num(2000)
    assert test_stocks_num == True

# test set_stock_price method
def test_set_stocks_price():
    test_stocks_price = c1.set_stock_price(25)
    assert test_stocks_price == True

# test set_comp_type method
def test_set_comp_type():
    test_comp_type = c1.set_comp_type("General")
    assert test_comp_type == True

# test update_net_worth method
def test_update_net_worth_1():
    test_updated_net_worth = c1.update_net_worth(0)
    assert test_updated_net_worth == False

def test_update_net_worth_2():
    test_updated_net_worth = c1.update_net_worth(2027.5)
    assert test_updated_net_worth == True

# test_add_stocks method
def test_add_stocks_1():
    added_stocks = c1.add_stocks(-850)
    assert added_stocks == False

def test_add_stocks_2():
    added_stocks = c1.add_stocks(8000)
    assert added_stocks == True

# test Operator Overloading

# create a new company ('other')
c2 = Company("Lenovo", 1000, 5, "High Tech")

# greater than operator
def test_gt_operator():
    assert (c1 > c2) == True

# less than operator
def test_lt_operator():
    assert (c1 < c2) == False

# equal to operator
def test_et_operator():
    assert (c1 == c2) == False

# test new company name 
def test_add_operator_1():
    new_company = c1 + c2
    assert new_company.name == "Google Two"

# test new company stocks number 
def test_add_operator_2():
    new_company = c1 + c2
    assert new_company.stocks_num == 9811

# test new company stock price
def test_add_operator_3():
    new_company = c1 + c2
    assert new_company.stock_price == 2.7548160228315157
           
# test new company type
def test_add_operator_4():
    new_company = c1 + c2
    assert new_company.comp_type == "General"

# test new company net worth
def test_add_operator_5():
    new_company = c1 + c2
    assert new_company.net_worth() == 27027.5


