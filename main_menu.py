def menu():
    print("======= MENU =======")
    print("[1] Books Dictionary")
    print("[2] Borrow List Dictionary")
    print("[3] Logbook Dictionary")
    print("====================")

def main():
    books = {}
    borrowed = {}
    log_book = {}

    while True:
        menu()

        choice = input("Enter option: ")
        print("====================")


        if choice == '1':
            from Books_Dictionary import main
            main()
        elif choice == '2':
            from Borrow_List_Dictionary import main
            main()
        elif choice == '3':
            from Logbook_Dictionary import main
            main()
        else:
            print("Invalid choice. Please enter a valid option.")

main()

