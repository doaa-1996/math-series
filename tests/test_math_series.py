from math_series import __version__
from math_series.math_series import fibonacci, lucas,sum_series

def test_version():
    assert __version__ == '0.1.0'


# 0, 1, 1, 2, 3, 5, 8, 13, ...
# 2, 1, 3, 4, 7, 11, 18, 29, ..


def test_0():
    assert fibonacci(0) ==0

    
def test_1():
    assert fibonacci(1) ==1

    
def test_2():
    assert fibonacci(2) ==1


def test_3():
    assert fibonacci(3) ==2   


def test_00():
    assert lucas(0) == 2


def test_11():
    assert lucas(1) == 1


def test_22():
    assert lucas(2) == 3


def test_33():
    assert lucas(3) == 4



def test_sum_series0():
    assert sum_series(0) == 0



def test_sum_series1():
    assert sum_series(1) == 1


def test_sum_series2():
    assert sum_series(2) == 1


def test_sum_series3():
    assert sum_series(3) == 2



def test_sum_series021():
    assert sum_series(0,2,1) == 2


def test_sum_series121():
    assert sum_series(1,2,1) == 1


def test_sum_series221():
    assert sum_series(2,2,1) == 3


def test_sum_series0712():
    assert sum_series(0,7,12)==7

def test_sum_series1712():
    assert sum_series(1,7,12)==12

def test_sum_series2712():
    assert sum_series(2,7,12)==19