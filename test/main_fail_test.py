import pytest
from src.utils import check_input

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
def test_employee_balance(wrong_input):
    assert check_input(wrong_input)

