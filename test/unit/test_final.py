import unittest
from unittest import mock
from unittest.mock import MagicMock

from final import Car, CarRental, CarPrice, SendReceipt

class TestCarRental(unittest.TestCase):
    def setUp(self):
        self.no_of_days = 10
        self.driver_age = 25
        self.mock_car = mock.create_autospec(Car)
        self.mock_car.car_class = "Compact"
        self.mock_car.car_year = 2022

    def test_car_rental_create_success(self):
        car_rental = CarRental(self.no_of_days, self.mock_car, self.driver_age)
        self.assertEqual(car_rental.no_of_days, self.no_of_days)
        self.assertEqual(car_rental.car, self.mock_car)
        self.assertEqual(car_rental.driver_age, self.driver_age)

    def test_car_rental_create_fail(self):
        with self.assertRaises(Exception) as exception:
            CarRental(
                self.no_of_days,
                self.mock_car,
                19
            )
        self.assertTrue("Driver must be atleast 21 years old to rent a car.")

class TestPriceService(unittest.TestCase):
    def setUp(self):
        self.mock_car = mock.create_autospec(Car)
        self.mock_car.no_of_seats = 5
        self.mock_car.year = 2020
        self.mock_car_rental = mock.create_autospec(CarRental)
        self.mock_car_rental.no_of_days = 10


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
                self.mock_car.car_class = context[0]
                self.mock_car_rental.car = self.mock_car
                self.mock_car_rental.driver_age = context[1]
                price = CarPrice.calculate_car_price(self.mock_car, self.mock_car_rental)
                self.assertEqual(price, expected)

class TestSendReceipt(unittest.TestCase):
    def test_send_email_to_purchaser(self):
        message = SendReceipt.email_receipt_to_purchaser()
        self.assertEqual(message, "Confirmed. Car Rental receipt has been emailed to purchaser")

class TestCar(unittest.TestCase):
    def setUp(self):
        self.car_class = "Compact"
        self.car_year = 2020
        self.no_of_seats = 5
        self.CAR_CLASSES = ['Compact', 'Luxury', 'SUV', 'Sport']

    def test_car_create_success(self):
        car = Car(self.car_class, self.car_year, self.no_of_seats)
        self.assertEqual(car.car_class, self.car_class)
        self.assertEqual(car.car_year, self.car_year)
        self.assertEqual(car.no_of_seats, self.no_of_seats)

    def test_car_create_fail_car_class(self):
        with self.assertRaises(Exception) as exception:
            Car(
                "Premium",
                self.car_year,
                self.no_of_seats
            )
        self.assertTrue(f'Must be one of classes: {", ".join(self.CAR_CLASSES)}' in str(exception.exception))
    
    def test_car_create_fail_year(self):
        with self.assertRaises(Exception) as exception:
            Car(
                self.car_class,
                2025,
                self.no_of_seats
            )
        self.assertTrue("Year must be current year or earlier" in str(exception.exception))
    
    def test_car_create_fail_no_of_seats(self):
        with self.assertRaises(Exception) as exception:
            Car(
                self.car_class,
                self.car_year,
                0
            )
        self.assertTrue("Seats must be greater than zero." in str(exception.exception))

