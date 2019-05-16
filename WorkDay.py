from utils import *
from ShiftTime import ShiftTime


class WorkDay:

    def __init__(self, day, init_time, end_time):
        self.init_shift = ShiftTime(day, init_time, True)
        self.end_shift = ShiftTime(day, end_time, False)

    def get_hours_payment(self, init_time, end_time, payment):
        diff_time = end_time - init_time
        return (diff_time.seconds/3600) * payment

    def calculate_shift_payment(self, shift):
        hour_cost = shift.hour_cost
        if shift.isFirstShiftWorked:
            init_time = shift.time
            end_time = shift.format_time(shift.closing_hours)
        else:
            init_time = shift.format_time(shift.opening_hours)
            end_time = shift.time
        return self.get_hours_payment(init_time, end_time, hour_cost)

    def calculate_total_payment(self):
        if self.end_shift.schedule == self.init_shift.schedule:
            init_time = self.init_shift.time
            end_time = self.end_shift.time
            hour_cost = self.init_shift.hour_cost
            return self.get_hours_payment(init_time, end_time, hour_cost)

        else:
            payment = 0
            init_shift_payment = self.calculate_shift_payment(self.init_shift)
            end_shift_payment = self.calculate_shift_payment(self.end_shift)
            payment = init_shift_payment + end_shift_payment
            if self.init_shift.schedule == 'morning' and self.end_shift.schedule == 'night':
                middle_shift = ShiftTime(self.init_shift.day, closing_schedule_hour['noon'], False)
                payment = payment + self.calculate_shift_payment(middle_shift)
            return payment
