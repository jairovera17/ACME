from datetime import datetime
import re

re_employee_name = '[A-Za-z]+'
re_day = '(MO|TU|WE|TH|FR|SA|SU)'
re_hour = '(([0-1][0-9]|2[0-3]):[0-5][0-9])'
re_time_worked = '{}-{}'.format(re_hour, re_hour)
re_workday = '{}{}'.format(re_day, re_time_worked)
re_employee_workday = '^{}={}(,{})*$'.format(re_employee_name, re_workday, re_workday)


def check_input(input_str):
    if re.match(re_employee_workday,input_str):
        matchobj = re.finditer(re_time_worked,input_str)
        for item in matchobj:
            if not item.group(1) < item.group(3):
                raise ValueError('Clock-In ({}) time cannot be equal or greater than Clock-out time ({})'.format(item.group(1),item.group(3)))
    else:
        raise Exception('Invalid Input')


def format_time(time_str):
    t_format = '%H:%M'
    zero_time = datetime.strptime('00:00', t_format)
    output = datetime.strptime(time_str, t_format) - zero_time
    return output

