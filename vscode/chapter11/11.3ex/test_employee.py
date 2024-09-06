from employee import Employee
import pytest

@pytest.fixture
def emp():
    emp = Employee("John", "Doe")
    return emp

'''
def test_give_default_raise():
    """测试默认加薪"""
    emp = Employee("John", "Doe")
    assert emp.salary == 5000
    original_salary = emp.salary
    emp.give_raise()
    assert emp.salary == original_salary + 5000


def test_give_custom_raise():
    """测试自定义加薪"""
    emp = Employee("Jane", "Doe")
    original_salary = emp.salary
    emp.give_raise(10000)
    assert emp.salary == original_salary + 10000
'''
def test_give_default_raise(emp):
    """测试默认加薪"""
    assert emp.salary == 5000
    original_salary = emp.salary
    emp.give_raise()
    assert emp.salary == original_salary + 5000


def test_give_custom_raise(emp):
    """测试自定义加薪"""
    original_salary = emp.salary
    emp.give_raise(10000)
    assert emp.salary == original_salary + 10000