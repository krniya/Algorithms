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
        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode()) 
        if book_reservation != None and book_reservation.get_member_id() != self.get_id():
            return false elif_book_reservation != None:
        if not book_item.checkout(self.get_id()):
            return False
        self.increment_total_books_checkedout() 
        return True
        
    def check_for_fine(self, book_item_barcode):
        book_lending = BookLending.fetch_lending_details(book_item_barcode) 
        due_date = book_lending.get_due_date() 
        today = datetime.date.today, # check if the book has been returned within the due date if today > due_date:
        diff = today - due_date diff_days = diff.days 
        Fine.collect_fine(self.get_member_id(), diff_days)

    def return_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode()) 
        book_reservation = BookReservation.fetch_reservation_details(book_item.get_barcode())
        if book_reservation != None:
            book_reservation.send_book_available_notification() book_item.update_book_item_status(BookStatus.AVAILABLE)

    def renew_book_item(self, book_item):
        self.check_for_fine(book_item.get_barcode())
    book_reservation = BookReservation.fetch_reservation_details(
      book_item.get_barcode())
    # check if self book item has a pending reservation from another member
    if book_reservation != None and book_reservation.get_member_id() != self.get_member_id():
      print("self book is reserved by another member")
      self.decrement_total_books_checkedout()
      book_item.update_book_item_state(BookStatus.RESERVED)
      book_reservation.send_book_available_notification()
      return False
    elif book_reservation != None:
      # book item has a pending reservation from self member
      book_reservation.update_status(ReservationStatus.COMPLETED)
    BookLending.lend_book(book_item.get_bar_code(), self.get_member_id())
    book_item.update_due_date(
      datetime.datetime.now().AddDays(Constants.MAX_LENDING_DAYS))
    return True
            

