from abc import ABC, abstractmethod
from datetime import datetime
from mimetypes import init
from Python.Design.LibraryManagement.DataElement import AccountStatus, Constants

class Account(ABC):
    def __init__(self,id,password,person,status= AccountStatus.ACTIVE) -> None:
        self.__id = id
        self.__password = password
        self.person = person
        self.status = status

    def resetPassword(self):
        None

class Librarian(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)

    def add_book_items(self, bookItems):
        pass

    def blockMember(self, member):
        pass

    def unBlockMember(self, member):
        pass


class Member(Account):
    def __init__(self, id, password, person, status=AccountStatus.ACTIVE) -> None:
        super().__init__(id, password, person, status)
        self.__dateOfMemberShip = datetime.date.today()
        self.__totalBooksCheckedOut = 0

    def getTotalBooksCheckedOut(self):
        return self.__totalBooksCheckedOut

    def increaseTotalBookCheckedOut(self):
        pass

    def checkoutBookItem(self, bookItem):
        if self.__totalBooksCheckedOut >= Constants.MAX_BOOK_PER_USER:
            print("User Already checked-out alloted max number of books")
            return False

        
            

