import unittest
from final import CarRental, CarPrice, Car

class TestCarRental(unittest.TestCase):
    def setUp(self):
        self.car_class = "Compact"
        self.car_year = 2022
        self.no_of_seats = 5
        self.car = Car(self.car_class, self.car_year, self.no_of_seats)
        self.no_of_days = 10
        self.driver_age = 25

    def test_car_rental_create_success(self):
        car_rental = CarRental(self.no_of_days, self.car, self.driver_age)
        self.assertEqual(car_rental.no_of_days, self.no_of_days)
        self.assertEqual(car_rental.car, self.car)
        self.assertEqual(car_rental.driver_age, self.driver_age)

    def test_car_rental_create_fail(self):
        with self.assertRaises(Exception) as exception:
            CarRental(
                self.no_of_days,
                self.car,
                19
            )
        self.assertTrue("Driver must be atleast 21 years old to rent a car.")

class TestPriceService(unittest.TestCase):
    def test_calculate_car_price(self):
        fixture_data = (
            (
                ["Luxury", 25], 1200,
            ),
            (
                ["Luxury", 21], 1320,
            ),
            (
                ["Luxury", 28], 1200,
            ),
            (
                ["Compact", 25], 800,
            ),
            (
                ["Compact", 21], 880,
            ),
            (
                ["Compact", 28], 800,
            ),
            (
                ["SUV", 25], 1100,
            ),
            (
                ["SUV", 21], 1210,
            ),
            (
                ["SUV", 28], 1100,
            ),
            (
                ["Sport", 25], 1800,
            ),
            (
                ["Sport", 21], 1980,
            ),
            (
                ["Sport", 28], 1800,
            ),
        )
        for context, expected in fixture_data:
            with self.subTest(context=context):
                self.car_class = context[0]
                self.car_year = 2020
                self.no_of_seats = 5
                self.car = Car(self.car_class, self.car_year, self.no_of_seats)
                self.no_of_days = 10
                self.driver_age = context[1]
                self.car_rental = CarRental(self.no_of_days, self.car, self.driver_age)
                price = CarPrice.calculate_car_price(self.car, self.car_rental)
                self.assertEqual(price, expected)
    