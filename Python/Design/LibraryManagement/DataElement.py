from enum import Enum
from re import L


class BookFormat(Enum):
    PaperBack, HardCover, AudioBook, EBook = 1,2,3,4

class BookStatus(Enum):
    Available, Reserved, NotAvailable = 1,2,3

class ReservationStatus(Enum):
    Waiting, Pending, Completed, Cancel = 1,2,3,4

class AccountStatus(Enum):
    Active, Closed, BlackListed = 1,2,3

class Address:
    def __init__(self, street, landmark, city, state, pin) -> None:
        self.street = street
        self.landmark = landmark
        self.city = city
        self.state = state
        self.pin = pin

class Person:
    def __init__(self, name, address, email, phone) -> None:
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        