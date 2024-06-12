log_book = {}

def menu():
    print("======= MENU =======")
    print("[1] Visit Library")
    print("[2] View All Entries")
    print("[3] View Transactions per Day")
    print("[4] Load Progress")
    print("[5] Save Progress")
    print("[6] Return to Main Menu")
    print("====================")


log_id_counter = 1

def visit_library(log_book):
    global log_id_counter
    person_name = input("Enter your name: ")
    date = input("Enter date today (e.g. 31 May 2023): ")
    time = input("Enter time visit (e.g. 9PM, 10:20AM): ")

    valid_purposes = ["borrow", "return", "visit"]
    
    while True:
        purpose = input("Enter your purpose of visit (borrow/return/visit): ")
        if purpose.lower() in valid_purposes:
            break
        else:
            print("Invalid purpose. Please enter 'borrow', 'return', or 'visit'.")

    log_ID = "L" + str(log_id_counter)

    log_book[log_ID] = {
            "Log ID": log_ID,
            "Name": person_name,
            "Date": date,
            "Time": time,
            "Purpose": purpose,
        }
    
    log_id_counter += 1
    
    print("====================")
    print("Logged in successfully!")
    print("Log ID:", log_ID)


def view_all_entries(log_book):
    if len(log_book) == 0:
        print("Sorry, logbook is empty.")
    else:
        for k, v in log_book.items(): #v is the dict
            for i, j in v.items(): #i is key and j is value
                print(f"{i}: {j}") #f string to format the string inside the curly braces
            print("====================")


def view_transactions(log_book):
    if len(log_book) == 0:
        print("Sorry, logbook is empty.")
    else:
        transaction_day = input("Enter date of transaction (e.g. 31 May 2023): ")

        transactions = [(log_ID, log_info) for log_ID, log_info in log_book.items() if
                        log_info.get("Date") == transaction_day]

        if not transactions:
            print("No transactions found for the given date.")
        else:
            print(f"==== Transactions on {transaction_day} ====")
            for log_ID, log_info in transactions:
                for i, j in log_info.items():
                    print(f"{i}: {j}")
                print("====================")


def loadPortfolio(log_book):
    readHandle = open("Logbook_Dictionary.txt", "r")
    for line in readHandle:
        data = line.strip().split(',')
        log_ID = data[0]
        person_name = data[1]
        date = data[2]
        time = data[3]
        purpose = data[4]

        log_book[log_ID] = {
            "Log ID": log_ID,
            "Name": person_name,
            "Date": date,
            "Time": time,
            "Purpose": purpose,
        }

    readHandle.close()
    print("Successfully loaded information")

def savePortfolio(log_book):
    fileHandle = open("Logbook_Dictionary.txt", "w")

    header_line = "Log ID,Name,Date,Time,Purpose\n"
    fileHandle.write(header_line)

    for log_id, data in log_book.items():
        line = f"{data['Log ID']},{data['Name']},{data['Date']},{data['Time']},{data['Purpose']}\n"
        fileHandle.write(line)
    
    fileHandle.close()
    print("Successfully saved information")


def main():
    while True:
        menu()
        choice = input("Enter option: ")
        print("====================")

        if choice == '1':
            visit_library(log_book)
        elif choice == '2':
            view_all_entries(log_book)
        elif choice == '3':
            view_transactions(log_book)
        elif choice == '4':
            loadPortfolio(log_book)
        elif choice == '5':
            savePortfolio(log_book)
        elif choice == '6':
            from main_menu import main
            main()
        else:
            print("Invalid choice. Please enter a valid option.")
