from enum import Enum
from abc import ABC
class BookFormat(Enum):
    PAPERBACK, HARDCOVER, AUDIOBOOK, EBOOK = 1,2,3,4

class BookStatus(Enum):
    AVAILABLE, RESERVED, NOTAVAILABLE = 1,2,3

class ReservationStatus(Enum):
    WAITING, PENDING, COMPLETED, CANCEL = 1,2,3,4

class AccountStatus(Enum):
    ACTIVE, CLOSED, BLACKLISTED = 1,2,3

class Address:
    def __init__(self, street, landmark, city, state, pin) -> None:
        self.__street = street
        self.__landmark = landmark
        self.__city = city
        self.__state = state
        self.__pin = pin

class Person(ABC):
    def __init__(self, name, address, email, phone) -> None:
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
        
class Constants:
    MAX_BOOK_PER_USER = 5
    MAX_LENDING_DAY = 10

