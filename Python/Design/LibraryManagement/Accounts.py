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

