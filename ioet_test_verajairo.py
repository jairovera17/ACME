import sys
from datetime import datetime


weekends = ['SA','SU']

payment = {
    'morning': 25,
    'noon': 15,
    'night': 20,
    ('weekend','morning'):30,
    ('weekend','noon'):20,
    ('weekend','night'):25
}

open_time = {
    'noon': 9 * 3600,
    'night': 18 * 3600,
    ('weekend','noon'):9 * 3600,
    ('weekend','night'):18 * 3600,
    
}
closing_time = {
    'morning': 9 * 3600,
    'noon': 18 * 3600,
    'night': 23 * 3600 + 59 * 60,
    ('weekend','morning'):9 * 3600,
    ('weekend','noon'):18 * 3600,
    ('weekend','night'):24 * 3600
    
}


def get_period(day,time_in_seconds):
    if 60 < time_in_seconds <= 9*3600:
        if day in weekends:
            return ('weekend','morning')
        return 'morning'

    elif 9*3600 + 60 < time_in_seconds <= 18*3600:
        if day in weekends:
            return ('weekend','noon')
        return 'noon'
    
    elif 18 * 3600 + 60 < time_in_seconds or (time_in_seconds < 60):
        if day in weekends:
            return ('weekend','night')
        return 'night'

def cost_until_period_closes(time_worked,time_period):

    return (closing_time[time_period] - time_worked)/3600 * payment[time_period]

def cost_until_time_worked(time_worked,time_period):

    return (time_worked - open_time[time_period])/3600 * payment[time_period]
    
def single_period_worked(time_worked, hour_cost):
    time_worked = time_worked.seconds / 3600
    return time_worked * hour_cost

def mixed_period_worked(init_time,init_period,end_time,end_period):
    pay = cost_until_period_closes(init_time,init_period)
    pay = pay+cost_until_time_worked(end_time,end_period)
    noon_periods = ['noon',('weekend','noon')]
    if init_period in noon_periods or end_period in noon_periods:
        return pay
    else:
        if init_period == 'morning' and end_period == 'night':
            return pay + 9 * payment['noon']
        elif init_period == ('weekend','morning') and end_period == ('weekend','night'):
            return pay + 9 * payment[('weekend','noon')]
        
def get_shift_pay(day_worked):
    day = day_worked[0:2]
    day_time = day_worked[2:].split('-')

    time_format = '%H:%M'
    zero_time = datetime.strptime('00:00', time_format)
    init_time = datetime.strptime(day_time[0], time_format) - zero_time
    end_time = datetime.strptime(day_time[1], time_format) - zero_time

    init_period = get_period(day,init_time.seconds)
    end_period = get_period(day,end_time.seconds)

    if payment[init_period] == payment[end_period]:
        return single_period_worked(end_time - init_time, payment[init_period])
    else:
        return mixed_period_worked(init_time.seconds,init_period,end_time.seconds,end_period)

        
def get_total_payment(total_time_worked):
    
    final_payment = 0

    for day_worked in total_time_worked:
        final_payment = final_payment + get_shift_pay(day_worked)

    return int(final_payment)

def get_employee_balance(input_data):
    employee_name = input_data.split('=')[0]
    total_time_worked = input_data.split('=')[1].split(',')
    total_payment = get_total_payment(total_time_worked)
    output = 'The amount to pay '+employee_name+' is: '+str(total_payment)+' USD'
    return output

    

if __name__ == '__main__' :
    
    try:
        print(get_employee_balance(sys.argv[1]))
    except:
        print('Error: Invalid Input')



