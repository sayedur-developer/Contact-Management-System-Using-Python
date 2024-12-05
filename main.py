import contact
import file_manager

def main_menu():
    while True:
        print("\n--- Contact Book Management ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Update Contact")
        print("4. Remove Contact")
        print("5. Search Contacts")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            contact.add_contact()
        elif choice == '2':
            contact.view_contacts()
        elif choice == '3':
            contact.update_contact()
        elif choice == '4':
            contact.remove_contact()
        elif choice == '5':
            contact.search_contacts()
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    file_manager.load_contacts()
    main_menu()
