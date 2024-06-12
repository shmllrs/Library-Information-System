borrowed = {}

def menu():
    print("======= MENU =======")
    print("[1] Borrow Book")
    print("[2] Return Book")
    print("[3] View All Entries")
    print("[4] View Expected Returns")
    print("[5] Load Progress")
    print("[6] Save Progress")
    print("[7] Return to Main Menu")
    print("====================")


borrowed_id_counter = 1 #uses global counter to track the string of borrowed ids to be listed down

def borrow_book(borrowed):
    global borrowed_id_counter 
    title_borrow = input("Enter book title to borrow: ")
    author_borrow = input("Enter author of the book: ")
    return_date = input("Enter date of return (e.g. 31 May 2023): ")

    borrow_ID = "BL" + str(borrowed_id_counter)

    borrowed[borrow_ID] = {
            "Borrow ID": borrow_ID,
            "Title": title_borrow,
            "Author": author_borrow,
            "Return Date": return_date,
    }
    
    borrowed_id_counter += 1

    if title_borrow in borrowed:
    # Update the status to "Unavailable" for the specified book
        books[title_borrow]["Status"] = "Unavailable"
        print(f"The book '{title_borrow}' is now marked as Unavailable.")
        print("====================")
        print("Book borrowed successfully!")
        print("Borrow ID:", borrow_ID)


def return_book(borrowed):
    for book_id, borrow_info in borrowed.items():
        if borrow_info.get("Status") == 'Borrowed' and log_book.get(book_id, {}).get("purpose") == 'return':
            # Update the status to "Available" for the returned book
            books[book_id]["Status"] = "Available"
            print("The book has been returned")
    return


from Books_Dictionary import books
from Logbook_Dictionary import log_book
def view_all_entries(borrowed):
    if len(borrowed) == 0:
        print("Sorry, there are no borrowed books at the moment.")
        return
    
    else:
        print("==== Borrowed Books ====")
        for k, v in borrowed.items(): #v is the dict
                for i, j in v.items(): #i is key and j is value
                    print(f"{i}: {j}")
                    print(books['Date Published'])
                    print(log_book['Name'])
                print("====================")


def view_expected_returns(borrowed):
    date_expected = input("Enter date of your expected returns (e.g. 31 May 2023) : ")
     
    if len(borrowed) == 0:
        print("Sorry, there are no borrowed books at the moment. ")
    
    else:
        for borrow_entry in borrowed.values():
            if borrow_entry["Return Date"] == date_expected:
                print("==== Expected Returns ====")
                for key, value in borrow_entry.items():
                    print(f"{key}: {value}")
                print("====================")
                return  # Exit the function after printing the expected returns

        # If no expected returns were found for the specified date
        print("Sorry, there are no expected returns from that date. ")


def loadPortfolio(borrowed):
    readHandle = open("Borrowed__List_Dictionary.txt", "r")
    for line in readHandle:
        data = line.strip().split(',')
        borrow_ID = data[0]
        title_borrow = data[1]
        author_borrow = data[2]
        return_date = data[3]

        borrowed[borrow_ID] = {
            "Borrow ID": borrow_ID,
            "Title": title_borrow,
            "Author": author_borrow,
            "Return Date": return_date,
        }

    readHandle.close()
    print("Successfully loaded information")

def savePortfolio(books):
    fileHandle = open("Borrowed__List_Dictionary.txt", "w")
    for borrow_id, data in borrowed.items():
        line = f"{'Borrow ID'},{'Title'},{'Author'},{'Return Date'}\n"
        fileHandle.write(line)
    
    fileHandle.close()
    print("Successfully saved information")


                
def main():
    while True:
        menu()
        choice = input("Enter option: ")
        print("====================")

        if choice == '1':
            borrow_book(borrowed)
        elif choice == '2':
            return_book(borrowed)
        elif choice == '3':
            view_all_entries(borrowed)
        elif choice == '4':
            view_expected_returns(borrowed)
        elif choice == '5':
            loadPortfolio(books)
        elif choice == '6':
            savePortfolio(books)
        elif choice == '7':
            from main_menu import main
            main()
        else:
            print("Invalid choice. Please enter a valid option.")




