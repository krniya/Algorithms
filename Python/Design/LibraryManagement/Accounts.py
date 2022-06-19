from abc import ABC, abstractmethod
from mimetypes import init
from Python.Design.LibraryManagement.DataElement import AccountStatus

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



