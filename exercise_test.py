import unittest
from ioet_test_verajairo import *
time_format = '%H:%M'
zero_time = datetime.strptime('00:00',time_format)


class ExerciseTest(unittest.TestCase):

    
    def test_period_worked_morning(self):
        self.assertEqual(get_period('MO',3600),'morning')
    def test_period_worked_night(self):
        self.assertEqual(get_period('MO',22*3600),'night')
    def test_period_worked__weekend_morning(self):
        self.assertEqual(get_period('SA',9*3600),('weekend','morning'))

    def test_single_period_worked(self): 
        test_time = datetime.strptime('5:00',time_format) - zero_time
        self.assertEqual(single_period_worked(test_time,payment['noon']),75)

    def test_mixed_two_period_worked(self):
        self.assertEqual(mixed_period_worked(8*3600,'morning',15*3600,'noon'),1*payment['morning']+6*payment['noon'])

    def test_mixed_all_day_period_worked(self):
        self.assertEqual(mixed_period_worked(7*3600,'morning',20*3600,'night'),2*payment['morning']+9*payment['noon']+2*payment['night'])

    def test_shift_pay(self):
        self.assertEqual(get_shift_pay('MO5:00-8:00'),3*payment['morning'])

    def test_employee_balance_all_day_shift(self):
        employee_jairo = 'JAIRO=MO10:00-20:00'
        self.assertEqual(get_employee_balance(employee_jairo),'The amount to pay JAIRO is: 160 USD')

    def test_employee_balance_astrid(self):
        employee_astrid = 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'
        self.assertEqual(get_employee_balance(employee_astrid),'The amount to pay ASTRID is: 85 USD')
    
    def test_employee_balance_rene(self):
        employee_rene = 'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        self.assertEqual(get_employee_balance(employee_rene),'The amount to pay RENE is: 215 USD')


if __name__ == '__main__':
    unittest.main()