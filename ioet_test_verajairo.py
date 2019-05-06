import sys
from datetime import datetime


weekends = ['SA', 'SU']

# un solo payment

hour_pay = {
    'morning': 25,
    'noon': 15,
    'night': 20,
    ('weekend', 'morning'): 30,
    ('weekend', 'noon'): 20,
    ('weekend', 'night'): 25
}

opening_time = {
    'noon': 9 * 3600,
    'night': 18 * 3600,
    ('weekend', 'noon'): 9 * 3600,
    ('weekend', 'night'): 18 * 3600,
    
}
closing_time = {
    'morning': 9 * 3600,
    'noon': 18 * 3600,
    'night': 23 * 3600 + 59 * 60,
    ('weekend','morning'): 9 * 3600,
    ('weekend','noon'): 18 * 3600,
    ('weekend','night'): 24 * 3600
    
}


def get_shift_schedule(day, time_in_seconds):
    if 60 < time_in_seconds <= 9*3600:
        if day in weekends:
            return ('weekend', 'morning')
        return 'morning'

    elif 9*3600 + 60 < time_in_seconds <= 18*3600:
        if day in weekends:
            return ('weekend', 'noon')
        return 'noon'

    elif 18 * 3600 + 60 < time_in_seconds or (time_in_seconds < 60):
        if day in weekends:
            return ('weekend', 'night')
        return 'night'


def pay_until_schedule_closes(time_worked, time_period):
    worked_hours = (closing_time[time_period] - time_worked)/3600
    return worked_hours * hour_pay[time_period]


def pay_until_time_worked(time_worked, time_period):
    worked_hours = (time_worked - opening_time[time_period])/3600
    return worked_hours * hour_pay[time_period]


def single_schedule_worked_pay(time_worked, hour_cost):
    time_worked = time_worked.seconds / 3600
    return time_worked * hour_cost


def multiple_schedules_worked_pay(init_time, init_schedule, end_time, end_schedule):
    pay = pay_until_schedule_closes(init_time, init_schedule)
    pay = pay+pay_until_time_worked(end_time, end_schedule)
    noon_periods = ['noon', ('weekend', 'noon')]
    if init_schedule in noon_periods or end_schedule in noon_periods:
        # Morning - Noon or Noon Night
        return pay
    else:
        if init_schedule == 'morning' and end_schedule == 'night':
            return pay + 9 * hour_pay['noon']
        elif init_schedule == ('weekend', 'morning') and end_schedule == ('weekend', 'night'):
            return pay + 9 * hour_pay[('weekend', 'noon')]


def get_worked_day_pay(worked_shift):
    worked_day = worked_shift[0:2]
    worked_hours = worked_shift[2:].split('-')

    t_format = '%H:%M'
    zero_time = datetime.strptime('00:00', t_format)
    init_time = datetime.strptime(worked_hours[0], t_format) - zero_time
    end_time = datetime.strptime(worked_hours[1], t_format) - zero_time

# get_shift_period  /// get_shift_schedule ?????
    init_schedule = get_shift_schedule(worked_day, init_time.seconds)
    end_schedule = get_shift_schedule(worked_day, end_time.seconds)

# shift[init] == shift[end]
# single shift /// multiple_shift
    if hour_pay[init_schedule] == hour_pay[end_schedule]:
        worked_time = end_time - init_time
        return single_schedule_worked_pay(worked_time, hour_pay[init_schedule])
    else:
        return multiple_schedules_worked_pay(init_time.seconds, init_schedule, end_time.seconds, end_schedule)


def get_total_payment_from_worked_shifts(total_shifts_worked):

    total_payment = 0
    for shift_worked in total_shifts_worked:
        total_payment = total_payment + get_worked_day_pay(shift_worked)
    return int(total_payment)


def get_employee_balance(input_data):

    employee_name = input_data.split('=')[0]
    total_worked_shifts = input_data.split('=')[1].split(',')
    total_payment = get_total_payment_from_worked_shifts(total_worked_shifts)
    string_output = 'The amount to pay '+employee_name+' is: '+str(total_payment)+' USD'
    return string_output


if __name__ == '__main__':

    try:
        print(get_employee_balance(sys.argv[1]))
    except:
        print('Error: Invalid Input')