import pytest
from WorkDay import WorkDay


@pytest.mark.parametrize(
    "day, init_time, end_time, expected",
    [
        ('MO','07:00','08:00',25),
        ('SU','07:00','08:00',30),
        ('WE','20:00','20:30',10),
        ('MO','08:00','10:00',40),

    ]
)  
def test_hours_payment(day,init_time, end_time, expected):
    work_day = WorkDay(day, init_time, end_time,)
    assert work_day.calculate_total_payment() == expected
