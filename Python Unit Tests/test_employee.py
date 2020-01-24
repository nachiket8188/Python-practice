import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setupClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        self.emp_1 = Employee('Nick', 'Totapholes', 15000)
        self.emp_2 = Employee('Sam', 'Witwicky', 21000)

    def tearDown(self):
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, "Nick.Totapholes@email.com")
        self.assertEqual(self.emp_2.email, "Sam.Witwicky@email.com")

        self.emp_1.first_name = 'John'
        self.emp_2.first_name = 'Jane'

        self.assertEqual(self.emp_1.email, "John.Totapholes@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Witwicky@email.com")

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, "Nick Totapholes")
        self.assertEqual(self.emp_2.fullname, "Sam Witwicky")

        self.emp_1.first_name = 'John'
        self.emp_2.first_name = 'Jane'

        self.assertEqual(self.emp_1.email, "John.Totapholes@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Witwicky@email.com")

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 15600)
        self.assertEqual(self.emp_2.pay, 21840)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with("http://company.com/{}/{}".format("Totapholes", "May"))
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('August')
            mocked_get.assert_called_with("http://company.com/{}/{}".format("Witwicky", "August"))
            self.assertEqual(schedule, 'Bad response!')


if __name__ == '__main__':
    unittest.main()
