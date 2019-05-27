import pytest
from src.utils import *


@pytest.mark.xfail(raises=Exception)
@pytest.mark.parametrize(
    "wrong_input",
    [
        ('RENE=MO15:00-12:00ewrqrz'),
        ('ASTRID=MO16:00-12:00,234324234SU20:00-21:00'),
    ]

)
def test_employee_balance(wrong_input):
    assert check_input(wrong_input)

@pytest.mark.xfail(raises=ValueError)
@pytest.mark.parametrize(
    "wrong_input",
    [
        ('RENE=MO15:00-10:00'),
        ('ASTRID=MO16:00-12:00'),
    ]

)
def test_employee_balance_value_error(wrong_input):
    assert check_input(wrong_input)


@pytest.mark.parametrize(
    "time_str,expected",
    [
        ('10:00',36000),
        ('12:00',43200)
    ]

)
def test_format_time(time_str, expected):
    output = format_time(time_str)
    assert output.seconds == expected


