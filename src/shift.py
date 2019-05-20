from src.workinghours_constants import schedules
from src.workinghours_constants import opening_schedule_hour, closing_schedule_hour
from src.utils import format_time

class Shift:

    def __init__(self, init_time, end_time):
        self.clock_in = ScheduleTime(init_time)
        self.clock_out = ScheduleTime(end_time)


class ScheduleTime:

    def __init__(self, time):
        self.time = format_time(time)
        self.schedule, self.opening_hour, self.closing_hour = self.get_schedule(time)

    def get_schedule(self, time):
        for schedule in schedules:
            if opening_schedule_hour[schedule] <= time <= closing_schedule_hour[schedule]:
                opening_hour = format_time(opening_schedule_hour[schedule])
                closing_hour = format_time(closing_schedule_hour[schedule])
                return schedule, opening_hour, closing_hour

