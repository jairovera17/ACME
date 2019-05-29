import pytest
from workday import WorkDay


@pytest.mark.parametrize(
    "day, init_time, end_time, expected",
    [
        ('MO','07:00','08:00',25),
        ('SU','07:00','08:00',30),
        ('WE','20:00','21:00',20),
        ('MO','08:00','10:01',40),
        ('MO','08:00','20:04',200)

    ]
)  
def test_work_day_total_payment(day,init_time, end_time, expected):
    work_day = WorkDay(day, init_time, end_time,)
    assert work_day.calculate_total_payment() == expected

