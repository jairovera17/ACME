from datetime import datetime
from utils import *


class ShiftTime:

    def __init__(self, day, time, isFirstShiftWorked):
        self.day = day
        self.time = self.format_time(time)
        self.isFirstShiftWorked = isFirstShiftWorked
        self.schedule = self.set_schedule(day, time)
        self.hour_cost = hour_cost_dicc[self.schedule]

    def format_time(self, time_str):
        t_format = '%H:%M'
        zero_time = datetime.strptime('00:00', t_format)
        output = datetime.strptime(time_str, t_format) - zero_time
        return output

    def set_schedule(self, day, time):
        weekends = ['SA', 'SU']
        schedules = ['morning', 'noon', 'night']
        for schedule in schedules:
            if opening_schedule_hour[schedule] <= time <= closing_schedule_hour[schedule]:
                self.opening_hours = opening_schedule_hour[schedule]
                self.closing_hours = closing_schedule_hour[schedule]
                if day in weekends:
                    return 'weekend_'+schedule
                else:
                    return schedule