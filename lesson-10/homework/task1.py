#Exception classes

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass

class MemberNotFoundException(Exception):
    pass


#Library manager app
class Book:
    def __init__(self, title, author, is_borrowed):
        self.title=title
        self.author=author
        self.is_borrowed=is_borrowed

    def __str__(self):
        return f"Book title: {self.title}\nAuthor: {self.author}\nStatus: {'Borrowed' if self.is_borrowed else 'Available'}"

class Member:
    def __init__(self, name, borrowed_books):
        self.name=name
        self.borrowed_books=borrowed_books

    def __str__(self):
         return f"Member: {self.name}\nBorrowed books: {self.borrowed_books}"
    
class Library:
    def __init__(self):
        self.books={}
        self.members={}

    def add_book(self, title:str, author:str, is_borrowed=False):
        if title in self.books:
            print(f"Book '{title}' already exists in the library.")
            return
        else:
            new_book=Book(title,author, is_borrowed)
            self.books[title]=new_book

    def add_member(self, name:str, borrowed_books=0):
        new_member=Member(name, borrowed_books)
        self.members[name]=new_member

    def borrow_book(self, title, member_name):
        if title not in self.books:
            raise BookNotFoundException('Book is not found')     
        
        if self.books[title].is_borrowed == True:
            raise BookAlreadyBorrowedException("Book is already by someone")
            
        if member_name not in self.members:
            raise MemberNotFoundException("Member is not exist")
            
        if self.members[member_name].borrowed_books>=3:
            raise MemberLimitExceededException("Member's limit is full, you can only borrow 3 books")

        else:
            self.members[member_name].borrowed_books+=1
            self.books[title].is_borrowed=True
            print(f"Book: {title} is given to Member: {member_name}")
    
    def return_book(self, title, member_name):
        if title not in self.books:
            raise BookNotFoundException('Book is not found')
            
        if member_name not in self.members:
            raise MemberNotFoundException("Member is not exist")
        else:
            self.books[title].is_borrowed=False
            self.members[member_name].borrowed_books-=1
            print(f"{title} has been successfully returned by {member_name}")
    
    def view_books(self):
        if not self.books:
            print('No books are found')
        else:
            for book in self.books.values():
                print(book)

    def view_members(self):
        if not self.members:
            print('No members are found')
        else:
            for mem in self.members.values():
                print(mem)

def main():
    library=Library()
    while True:
        print("\nWelcome to the our Library manager app! ")
        print("1. Add new member")
        print("2. Add new book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. View all books")
        print("6. View all members")
        print("7. Exit")

        choice=int(input('Enter your choice:  '))

        if choice == 1:
            name=input("Enter the member\s name:  ")
            library.add_member(name)

        elif choice == 2:
            title=input("Enter the book title:  ")
            author=input('Enter the book author:  ')
            library.add_book(title,author)

        elif choice == 3:
            member_name=input('Enter the member name: ')
            title=input("Enter the book title:  ")
            library.borrow_book(title,member_name)

        elif choice == 4:
            member_name=input('Enter the member name: ')
            title=input("Enter the book title:  ")
            library.return_book(title,member_name)

        elif choice == 5:
            library.view_books()

        elif choice == 6:
            library.view_members()

        elif choice == 7:
            print('Exiting the program...')
            break

        else:
            print('Invalid choice, please try again')

    
if __name__ == "__main__":
    main()