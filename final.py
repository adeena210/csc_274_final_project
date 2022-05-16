# Adeena Ahmed
# CSC 275
# Spring 2022
# Final Project

class CarRental:
    """
    This is a class for a car rental period. 
    It contains details about a car rental period including number of days, details about the car (using the Car class), and age of the driver.
    """
    MINIMUM_AGE = 21

    def __init__(self, no_of_days, car, driver_age):
        self.no_of_days = no_of_days
        self.car = car
        self.driver_age = driver_age

    @property
    def driver_age(self):
            return self._driver_age

    @driver_age.setter
    def driver_age(self, age):
        if age < CarRental.MINIMUM_AGE:
            raise ValueError("Driver must be atleast 21 years old to rent a car.")
        self._driver_age = age

class CarPrice:
    """
    This class calculates the price of a Car Rental period using the CarRental class
    """
    BASE_PRICE = 80
    LUXURY_EXTRA_PRICE = 40
    SUV_EXTRA_PRICE = 30
    SPORT_EXTRA_PRICE = 100

    YOUNG_DRIVER_FEE_PERCENT = 10
    @staticmethod
    def calculate_car_price(self, car_rental):
        price_per_day = CarPrice.BASE_PRICE
        if car_rental.car.car_class == "Luxury":
            price_per_day += CarPrice.LUXURY_EXTRA_PRICE
        elif car_rental.car.car_class == "SUV":
            price_per_day += CarPrice.SUV_EXTRA_PRICE
        elif car_rental.car.car_class == "Sport":
            price_per_day += CarPrice.SPORT_EXTRA_PRICE

        if car_rental.driver_age < 25:
            price_per_day += price_per_day * (CarPrice.YOUNG_DRIVER_FEE_PERCENT/100)

        total_price = price_per_day * car_rental.no_of_days

        return total_price


class SendReceipt:
    """
    This class sends a receipt to the customer that includes the price of their rental period.
    """

    @staticmethod
    def email_receipt_to_purchaser():
        return 'Confirmed. Car Rental receipt has been emailed to purchaser'

class Car:
    """
    This class is for a Car. It includes details about its class, year, and number of seats.
    """
    CAR_CLASSES = ['Compact', 'Luxury', 'SUV', 'Sport']
    CURRENT_YEAR = 2022

    def __init__(self, car_class, car_year, no_of_seats):
        self.car_class = car_class
        self.car_year = car_year
        self.no_of_seats = no_of_seats

    @property
    def car_class(self):
        return self._car_class
    
    @car_class.setter
    def car_class(self, car_class):
        if car_class not in Car.CAR_CLASSES:
            raise ValueError(f'Must be one of classes: {", ".join(Car.CAR_CLASSES)}')
        self._car_class = car_class

    @property
    def car_year(self):
        return self._car_year

    @car_year.setter
    def car_year(self, year):
        if year > Car.CURRENT_YEAR:
            raise ValueError("Year must be current year or earlier")
        self._car_year = year

    @property
    def no_of_seats(self):
        return self._no_of_seats

    @no_of_seats.setter
    def no_of_seats(self, seats):
        if seats <= 0:
            raise ValueError("Seats must be greater than zero.")
        self._no_of_seats = seats

            
    












