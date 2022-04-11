from utils import database

USER_CHOICE = """
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """

def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()

        elif user_input == 'l':
            list_books()

        elif user_input == 'r':
            prompt_read_book()

        elif user_input == 'd':
            prompt_delete_book()
            
        else:
            print("Invalid input! please trt again")

        user_input = input(USER_CHOICE)
        
        

def prompt_add_book():
    name = input("Enter the name of the book? ")
    author = input("Enter the author of the book? ")

    database.add_book(name, author)

def list_books():
    books = database.get_all_books()

    for book in books:
        read = "Yes" if book['read'] == '1' else "No"
        print(f" '{book['name']}' by {book['author']},  {read}")

def prompt_read_book():
    name = input("Enter the name of the book you wish to mark as read? ")

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of the book you wish to delete? ")

    database.delete_book(name)



menu()