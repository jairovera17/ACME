import pytest
from src.shift import ScheduleTime
from src.shift import Shift
from src.utils import format_time

@pytest.mark.parametrize(
    "time, expected",
    [
        ('10:00','noon'),
        ('20:00','night'),
        ('23:00','night'),
        ('05:00','morning')
    ]
)
def test_schedule_time_schedule(time, expected):
    s_time = ScheduleTime(time)
    assert s_time.schedule == expected

@pytest.mark.parametrize(
    'time, expected',
    [
        ('10:00', '09:01'),
        ('12:00', '09:01'),
        ('21:00', '18:01'),
        ('01:00', '00:01')

    ]
)
def test_schedule_time_opening_time(time, expected):
    s_time = ScheduleTime(time)
    expected_time = format_time(expected)
    assert s_time.opening_hour.seconds == expected_time.seconds

@pytest.mark.parametrize(
    'time, expected',
    [
        ('10:00', '18:00'),
        ('12:00', '18:00'),
        ('21:00', '23:59'),
        ('01:00', '09:00')

    ]
)
def test_schedule_time_clousing_time(time, expected):
    s_time = ScheduleTime(time)
    expected_time = format_time(expected)
    assert s_time.closing_hour.seconds == expected_time.seconds


@pytest.mark.parametrize(
    'init_time, end_time, init_expected, end_expected',
    [
        ('10:00', '11:00','noon','noon'),
        ('12:00', '20:00', 'noon', 'night'),
        ('01:00', '08:00', 'morning', 'morning'),
        ('01:00', '22:00', 'morning', 'night')

    ]
)
def test_shift_schedules(init_time, end_time, init_expected, end_expected):
    shift = Shift(init_time, end_time)
    assert shift.clock_in.schedule == init_expected
    assert shift.clock_out.schedule == end_expected

