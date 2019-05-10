import pytest
from WorkDay import ShiftTime
from datetime import datetime


@pytest.mark.parametrize(
    "day, hour, expected",
    [
        ('MO', '10:00', 15),
        ('SU', '10:00', 20),
        ('WE', '20:00', 20)
    ]
)
def test_shift_time_hour_cost(day, hour, expected):
    shift = ShiftTime(day, hour, True)
    assert shift.hour_cost == expected


@pytest.mark.parametrize(
    "day, hour, expected",
    [
        ('MO', '10:00', 'noon'),
        ('SU', '05:00', 'weekend_morning'),
        ('SA', '23:00', 'weekend_night')
    ]
)
def test_set_schedule(day, hour, expected):
    shift = ShiftTime(day, hour, True)
    assert shift.schedule == expected

@pytest.mark.parametrize(
    "day, hour, expected",
    [
        ('MO', '10:00', '18:00'),
        ('SU', '05:00', '09:00'),
        ('SA', '23:00', '23:59')
    ]
)
def test_set_clousing_hours(day, hour, expected):
    shift = ShiftTime(day, hour, True)
    assert shift.closing_hours == expected


