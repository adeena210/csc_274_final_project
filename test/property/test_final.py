import unittest
from hypothesis import given, strategies as st
from final import Car

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car_class = "Compact"
        self.car_year = 2020
        self.no_of_seats = 5
        self.car = Car(self.car_class, self.car_year, self.no_of_seats)
        self.CURRENT_YEAR = 2022

    @given(year=st.integers(max_value = 2022))
    def test_car_year(self, year):
        self.car.car_year = year
        self.assertEqual(self.car.car_year, year)

    @given(no_of_seats = st.integers(min_value = 1))
    def test_car_seats(self, no_of_seats):
        self.car.no_of_seats = no_of_seats
        self.assertEqual(self.car.no_of_seats, no_of_seats)


