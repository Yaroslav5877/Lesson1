
from lesson_4.calculator import Calculator

calculator = Calculator()

def test_sum_positive_nums():
    calculator = Calculator
    res = calculator.sum(4, 5)
    assert res == 9

def test_sum_negative_nums():
    calculator = Calculator
    res = calculator.sum(-6, -10)
    assert res == -16

def test_sum_positive_and_negative_nums():
    calculator = Calculator
    res = calculator.sum(-6, 6)
    assert res == 0

# print("start")
# res = calculator.sum(4, 5)
# assert res == 9
# print(res)

# res = calculator.sum(-6, -10)
# assert res == -16
# print(res)

# res = calculator.sum(-6, 6)
# assert res == 0
# print(res)

# res = calculator.sum(1.2, 6.3)
# res = round(res, 1)
# assert res == 7.5
# print(res)


# res = calculator.sum(10, 0)
# assert res == 10
# print(res)

# res = calculator.div(10, 2)
# assert res == 5
# print(res)

# res = calculator.div(6, 0)
# assert res == None
# print(res)


# res = calculator.sum(-6, 6)
# assert res == 0
# print(res)
# print('finish')