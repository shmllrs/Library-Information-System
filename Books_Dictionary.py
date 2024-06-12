books = {}

def menu():
    print("======= MENU =======")
    print("[1] Add Book")
    print("[2] Delete Book")
    print("[3] Delete All Books")
    print("[4] View Books")
    print("[5] Edit Book")
    print("[6] View Pending Books")
    print("[7] Load Progress")
    print("[8] Save Progress")
    print("[9] Return to Main Menu")
    print("====================")


book_id_counter = 1 #uses global counter to track the string of book ids to be listed down

def add_book(books):
    global book_id_counter #call out global variable
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    date_published = input("Enter the date the book was published (e.g. 31 May 2023): ")

    book_id = "B" + str(book_id_counter) #initialize book id

    #contents of dictionary
    books[book_id] = {
        "Book ID": book_id,
        "Title": title,
        "Author": author,
        "Date Published": date_published,
        "Status": "Available",
        "Borrowers": [], 
    }
    
    #increment 
    book_id_counter += 1
    
    from Borrow_List_Dictionary import borrowed
    books[book_id]["Borrowers"].append(borrowed)

    print("====================")
    print("Book added successfully!")
    print("Book ID:", book_id)


def delete_book(books):
    if len(books) == 0:
        print("Sorry, there are no stored books yet in the inventory. Please add book/s.")
        return
    
    else:
        print("==== Books in the Inventory ====")
        for k, v in books.items(): 
                for i, j in v.items(): 
                    print(f"{i}: {j}")
                print("====================")

    del_title_book = input("Enter the title of the book you wanted to delete: ")
    del_author_book = input("Enter the author of the book: ")

    #checking if input is at the dictionary the book_id (id), book_info (info in dict) is a tupple where it checks or 
    #iterates in the books.items and checks if the input author and the title is at the dict
    check_books = [(book_id, book_info) for book_id, book_info in books.items() if
                   book_info.get("Title", "") == del_title_book and book_info.get("Author", "") == del_author_book]

    if check_books == 0:
        print("Title book entered", del_title_book, "and author", del_author_book, "is not found in the inventory." )
    else:
        # Ask user to confirm deletion
        confirmation = input("Do you want to delete this book (yes/no)? ").lower()
        if confirmation == 'yes':
            # Delete found books
            for book_id, _ in check_books: #the _ is for not looping the said value
                del books[book_id]
            print("Book deleted successfully.")
        else:
            print("Deletion canceled.")


def delete_all(books):
    confirmation = input("Are you sure you want to clear the inventory (yes/no)? ").lower()
    if confirmation == 'yes':
        books.clear()
        print("====================")
        print("The inventory is now empty.")
    else:
        return


def view_book(books):
    if len(books) == 0:
        print("Sorry, there are no stored books yet in the inventory. Please add book/s.")
    else:
        want_to_view = input("Enter the title of the book you want to view: ")

        check_books = {book_id: book_info for book_id, book_info in books.items() if
                       book_info.get("Title", "") == want_to_view}

        if not check_books:
            print("Entered book title is not in the inventory")
        else:
            for book_id, book_info in check_books.items():
                for key, value in book_info.items():
                    print(f"{key}: {value}")
                print("====================")



def edit_book(books):
    if len(books) == 0:
        print("Sorry, there are no stored books yet in the inventory. Please add book/s.")

    else:
        print("==== Books in the Inventory ====")
        for k, v in books.items(): 
                for i, j in v.items(): #i is key and j is value
                    print(f"{i}: {j}")
                print("====================")

        edit = input("Enter the book you want to edit: ")
        
        #checking if input is at the dictionary the book_id (id), book_info (info in dict) is a tupple where it checks or 
        #iterates in the books.items and checks if the input author and the title is at the dict
        check_books = [(book_id, book_info) for book_id, book_info in books.items() if
                    book_info.get("Title", "") == edit]
        

        if check_books == 0:
            print("Entered book title is not in the inventory")
        else:
            for book_id, book_info in check_books:
                for i, j in v.items(): #i is key and j is value
                        print(f"{i}: {j}")
                print("====================")
                
                new_title = input("Enter new title of the book: ")
                new_author = input("Enter new author of the book: ")
                new_date = input("Enter new date published of the book: ")

                #updating
                books[book_id]["Title"] = new_title
                books[book_id]["Author"] = new_author
                books[book_id]["Date Published"] = new_date

                print(edit, "is successfully edited.")


def view_pending(books):
    pending_books = [(book_id, book_info) for book_id, book_info in books.items() if
                     book_info.get("Status", "") == "Unavailable"]

    if len(pending_books) == 0:
        print("No pending books.")

    else:
        print("==== Pending Books ====")
        for book_id, book_info in pending_books():
            for key, value in book_info.items():
                print(f"{key}: {value}")
                print("====================")
                print("====================")
                from Logbook_Dictionary import log_book
                print(log_book["purpose"])
                from Borrow_List_Dictionary import borrowed
                print(borrowed["Return Date"])
            print("====================")


def loadPortfolio(books):
    readHandle = open("Books_Dictionary.txt", "r")
    for line in readHandle:
        data = line.strip().split(',')
        book_id = data[0]
        title = data[1]
        author = data[2]
        date_published = data[3]
        status = data[4]
        borrowers = data[5]

        books[book_id] = {
            "Book ID": book_id,
            "Title": title,
            "Author": author,
            "Date Published": date_published,
            "Status": status,
            "Borrowers": borrowers,
        }

    readHandle.close()
    print("Successfully loaded information")

def savePortfolio(books):
    fileHandle = open("Books_Dictionary.txt", "w")
    for book_id, data in books.items():
        line = f"{data['Book ID']},{data['Title']},{data['Author']},{data['Date Published']},{data['Status']},{data['Borrowers']}\n"
        fileHandle.write(line)
    
    fileHandle.close()
    print("Successfully saved information")


def main():
    while True:
        menu()
        choice = input("Enter option: ")
        print("====================")

        if choice == '1':
            add_book(books)
        elif choice == '2':
            delete_book(books)
        elif choice == '3':
            delete_all(books)
        elif choice == '4':
            view_book(books)
        elif choice == '5':
            edit_book(books)
        elif choice == '6':
            view_pending(books)
        elif choice == '7':
            loadPortfolio(books)
        elif choice == '8':
            savePortfolio(books)
        elif choice == '9':
            from main_menu import main
            main()
        else:
            print("Invalid choice. Please enter a valid option.")

