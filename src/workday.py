from workinghours_constants import regular_hour_cost, special_hour_cost
from workinghours_constants import weekends
from workinghours_constants import schedules
from workinghours_constants import opening_schedule_hour, closing_schedule_hour
from shift import Shift
from utils import format_time


class WorkDay:

    def __init__(self, day, init_time, end_time):
        self.day = day
        self.shift = Shift(init_time, end_time)
        self.hour_cost = regular_hour_cost
        if self.day in weekends:
            self.hour_cost = special_hour_cost

    def get_hours_payment(self, init_time, end_time, payment):
        diff_time = end_time - init_time
        time_worked = diff_time.seconds/3600.0
        return int(time_worked * payment)

    def calculate_total_payment(self):
        arrival = self.shift.clock_in
        departure = self.shift.clock_out
        hour_cost = self.hour_cost[arrival.schedule]
        if arrival.schedule == departure.schedule:
            return self.get_hours_payment(arrival.time, departure.time, hour_cost)
        else:
            payment = self.get_hours_payment(arrival.time,arrival.closing_hour,hour_cost)
            arrival_schedule_index = schedules.index(arrival.schedule)
            for schedule in schedules[arrival_schedule_index+1:]:
                hour_cost = self.hour_cost[schedule]
                if schedule == departure.schedule:
                    return payment + self.get_hours_payment(departure.opening_hour, departure.time,hour_cost)
                else:
                    init_time = format_time(opening_schedule_hour[schedule])
                    end_time = format_time(closing_schedule_hour[schedule])
                    payment = payment + self.get_hours_payment(init_time,end_time,hour_cost)

