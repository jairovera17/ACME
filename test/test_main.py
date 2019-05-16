import pytest
from ioet_test_verajairo import get_employee_balance

@pytest.mark.parametrize(
    "input, expected",
    [
        ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00','The amount to pay RENE is: 215 USD'),
        ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00','The amount to pay ASTRID is: 85 USD')
    ]

)
def test_employee_balance(input,expected):
    balance = get_employee_balance(input)
    assert balance == expected

