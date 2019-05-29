import sys
from workday import WorkDay
from utils import check_input

def get_day_payment(worked_day):
    day_name = worked_day[0:2]
    worked_time = worked_day[2:].split('-')
    worked_day = WorkDay(day_name, worked_time[0], worked_time[1])
    return worked_day.calculate_total_payment()


def calculate_final_payment(total_worked_days):
    total_payment = 0
    for worked_day in total_worked_days:
        total_payment = total_payment + get_day_payment(worked_day)
    return int(total_payment)


def get_employee_balance(input_data):
    employee_name = input_data.split('=')[0]
    total_worked_days = input_data.split('=')[1].split(',')
    final_payment = calculate_final_payment(total_worked_days)
    output_str = 'The amount to pay {} is: {} USD'.format(employee_name,str(final_payment))
    return output_str


if __name__ == '__main__':
    try:
        user_input = sys.argv[1]
        check_input(user_input)
        print(get_employee_balance(user_input))
    except Exception as error:
        print('Error:', error)

