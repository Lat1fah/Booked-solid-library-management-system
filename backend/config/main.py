#Library management system using python OOP 

class Book:
    def __init__(self,title,author): #so every book needs to have these details
        self.title=title
        self.author=author
        self.issued=False #we start the issued part on false, so there's no book that's checked out.

class Library: #so books are consolidated in the library. so this library class takes care of that. 
    def __init__(self):
        self.books=[] #start with an empty list
    
    def add_book(self,book): #this method makes it such that it can receieve books
        self.books.append(book) #this appends the empty book list.
        print(f"'{book.title}' added successfully!") 
    
    def show_books(self):
        if not self.boks: #this line checks if the book list is empty
            print("You don't have any books in your list.")
            return 
        print("\n=========Book List==========")
        for book in self.books:
            status="Issued" if book.issued else "Available"
            print(f"Title: {book.title} | Author: {book.author} | Status: {status}")
   
    def issue_book(self, title):  #this takes care of issuing books. Though I need to integrate a process where the e-book is always available
        for book in self.books:
            if book.title.lower()==title.lower(): 
                if not book.issued:
                    book.issued=True 
                    print(f"'{book.title}' issued successfully.")
                    return
                else:
                    print(f"'{book.title}' is already issued")

    def return_book(self, title): #this isn't supposed to be a thing because once a reader already downloads a free ebook then there's no point in returning it.
        for book in self.books: #It will stay for now, just for the flow. 
            if book.title.lower()==title.lower():
                if not book.isued:
                    book.issued=False
                    print(f"'{book.title}' returned successfully.")
                    return
                else:
                    print(f"'{book.title}' was not issued.")

    def search_book(self, title): #this enables users to search for books to add to their lists. 
        for book in self.books:
            if book.title.lower()== title.lower():
                status="Issued" if book.issued else "Available"
                print("\nBook Found")
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Status: {book.status}")
                return
            print("Book not found")

    def remove_book(self, title): #this removes the book from the list
        for book in self.books:
            if book.title.lower()== title.lower():
                self.books.remove(book)
                print(f"'{book.title} was removed.")
                return
            print("Book not found")

library= Library()
while True: #I HATE using the while loop. 
    print("\n=============BOOKED SOLID LIBRARY==============")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Search Book")
    print("6. Remove Book")
    print("7. Exit")
    choice= input("Enter your choice ")
    if choice == "1":
        title=input("Enter Book Title: ")
        author=input("Enter Author Name: ")
        book=Book(title, author)
        library.add_book(book)
    elif choice=="2":
        library.show_books()
    elif choice=="3":
        title=input("Which book would you like? :")
        library.issue_book(title)
    elif choice=="4":
        title=input("Which book would you like to return? :")
        library.issue_book(title)
    elif choice=="5":
        title=input("Which book are you looking for? Let us help! ")
        library.search_book(title)
    elif choice=="6":
        title=input("which book would you like to remove from your list? ")
        library.remove_book(title)
    elif choice=="7":
        print("Thank you! ")
        break 


git rm --cached backend
rm -rf backend/.git
git add .

git rm -r --cached env
printf "env/\n__pycache__/\n*.pyc\n.env\ndb.sqlite3\n" > .gitignore
git add .
git status