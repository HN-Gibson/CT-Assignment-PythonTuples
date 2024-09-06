# Task 1: Library System Enhancement Sharpen your skills in managing and modifying data within tuples and lists.

# Problem Statement: You are maintaining a library system where each book is stored as a tuple within a list. Your task is to update this system by adding new books and ensuring no duplicates.

# - Add functionality to insert new books into `library`. Ensure that adding a duplicate book is handled appropriately.

#create a function the adds a new book as a tuple to the list while checking for duplicate
def add_book(title,author):
    new_book=(title,author)
    if new_book not in library:
        library.append(new_book)
        print(f"{title} by {author} added to the library!")
    else:
        print(f"{title} by {author} already exists in the library.\nPlease try adding a different book.")

#create a function the prints the collection in a readable format
def view_collection (list):
    for title,author in list:
        print(f"{title} by {author}")

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

#create a while loop with exit, add new book, and view collection options
while True:
    user_request=input("Please enter a command from the list below:\n-Add Book\n-View Collection\n-Quit\n").lower
    if user_request() == "quit":
        break
    #call a function in if statements to add a book and one to view the collection
    elif user_request() == "add book":
        title = input("What is the title of the Book?\n")
        author = input(f"Who wrote {title}?\n")
        add_book(title,author)
    elif user_request() == "view collection":
        view_collection(library)
    else:
         print ("Invalid entry. Please type an option as listed.\n(Not Case Sensitive)")




