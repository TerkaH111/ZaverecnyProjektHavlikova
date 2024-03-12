import unittest
from insurance_app import InsuranceApp
from insured_person import InsuredPerson

class TestInsuranceApp(unittest.TestCase):
    def setUp(self):
        self.app = InsuranceApp()

    def test_valid_name(self):
        self.assertTrue(self.app.valid_name("Jan Novák"))
        self.assertFalse(self.app.valid_name("J4n"))

    def test_phone_number_validation(self):
        self.assertTrue(self.app.phone_number_validation("123456789"))
        self.assertFalse(self.app.phone_number_validation("12345"))


if __name__ == '__main__':
    unittest.main()
