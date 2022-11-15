from Company import Company

""" Company Tests """

# create Company instance
c1 = Company("Google", 1000, 20.284, "High Tech")


# test net_worth method
def test_net_worth():
    assert c1.net_worth() == 20284.0


# test set_name method
def test_set_name_1():
    assert c1.set_name("Google2") is False


def test_set_name_2():
    assert c1.set_name("Google Two") is True


# test set_stocks_num method
def test_set_stocks_num():
    assert c1.set_stocks_num(2000) is True


# test set_stock_price method
def test_set_stocks_price():
    assert c1.set_stock_price(25) is True


# test set_comp_type method
def test_set_comp_type():
    assert c1.set_comp_type("General") is True


# test update_net_worth method
def test_update_net_worth_1():
    assert c1.update_net_worth(0) is False


def test_update_net_worth_2():
    assert c1.update_net_worth(2027.5) is True


# test_add_stocks method
def test_add_stocks_1():
    assert c1.add_stocks(-850) is False


def test_add_stocks_2():
    added_stocks = c1.add_stocks(8000)
    assert added_stocks is True

# test Operator Overloading

# create a new company ('other')

c2 = Company("Lenovo", 1000, 5, "High Tech")


# greater than operator
def test_gt_operator():
    assert (c1 > c2) is True


# less than operator
def test_lt_operator():
    assert (c1 < c2) is False


# equal to operator
def test_et_operator():
    assert (c1 == c2) is False


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