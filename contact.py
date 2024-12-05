import file_manager
import utils

contacts = file_manager.load_contacts()

def add_contact():
    print("\n--- Add a New Contact ---")
    first_name = input("Enter First Name (mandatory): ").strip()
    if not utils.is_valid_name(first_name):
        print("Invalid First Name! Only letters, spaces, and dots are allowed.")
        return

    last_name = input("Enter Last Name (optional): ").strip()
    if last_name and not utils.is_valid_name(last_name):
        print("Invalid Last Name! Only letters, spaces, and dots are allowed.")
        return

    phone = input("Enter Phone Number (mandatory): ").strip()
    if not utils.is_valid_phone(phone):
        print("Invalid Phone Number! Must be 10 digits.")
        return

    country_code = input("Enter Country Code (default +880): ").strip() or "+880"
    if not utils.is_valid_country_code(country_code):
        print("Invalid Country Code!")
        return

    full_phone = f"{country_code}{phone}"
    if any(contact['phone'] == full_phone for contact in contacts):
        print("This phone number is already assigned to another contact.")
        return

    email = input("Enter Email (optional): ").strip()
    if email and not utils.is_valid_email(email):
        print("Invalid Email Address!")
        return

    address = input("Enter Address (optional): ").strip()
    
    new_contact = {
        "name": f"{first_name} {last_name}".strip(),
        "phone": full_phone,
        "email": email,
        "address": address
    }
    contacts.append(new_contact)
    file_manager.save_contacts(contacts)
    print("Contact added successfully!")

def view_contacts():
    print("\n--- View All Contacts ---")
    if not contacts:
        print("No contacts found.")
        return
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, "
              f"Email: {contact['email']}, Address: {contact['address']}")

def update_contact():
    """
    Update an existing contact's details by searching using the phone number.
    Allows updating name, phone, email, and address.
    If a field is left blank, the existing value is retained.
    """
    if not contacts:
        print("No contacts found.")
        return

    # Prompt the user to enter a phone number to find the contact
    search_phone = input("Enter the phone number of the contact to update: ").strip()

    # Locate the contact using the phone number
    matched_contact = next((contact for contact in contacts if contact['phone'] == search_phone), None)
    
    if not matched_contact:
        print("No contact found with the given phone number.")
        return

    print(f"\nFound Contact: Name: {matched_contact['name']}, "
          f"Phone: {matched_contact['phone']}, Email: {matched_contact['email']}, "
          f"Address: {matched_contact['address']}")
    print("\nLeave fields blank to keep current values.")

    # Update fields
    first_name = input(f"First Name ({matched_contact['name']}): ").strip()
    if first_name:
        if not utils.is_valid_name(first_name):
            print("Invalid First Name! Keeping the existing value.")
        else:
            matched_contact['name'] = first_name

    phone = input(f"Phone Number (with or without country code) ({matched_contact['phone']}): ").strip()
    if phone:
        if utils.is_valid_phone(phone):  # Handle 10-digit number
            country_code = input("Enter Country Code (default +880): ").strip() or "+880"
            if utils.is_valid_country_code(country_code):
                matched_contact['phone'] = f"{country_code}{phone}"
            else:
                print("Invalid Country Code! Keeping the existing phone.")
        elif utils.is_valid_full_phone(phone):  # Handle full number with country code
            matched_contact['phone'] = phone
        else:
            print("Invalid phone number format! Keeping the existing phone.")

    email = input(f"Email ({matched_contact['email']}): ").strip()
    if email:
        if not utils.is_valid_email(email):
            print("Invalid Email! Keeping the existing value.")
        else:
            matched_contact['email'] = email

    address = input(f"Address ({matched_contact['address']}): ").strip()
    if address:
        matched_contact['address'] = address

    # Save updates to the file
    file_manager.save_contacts(contacts)
    print("Contact updated successfully!")


def remove_contact():
    """
    Remove a contact by searching for its phone number.
    """
    if not contacts:
        print("No contacts found.")
        return

    # Prompt the user to enter a phone number to delete the contact
    search_phone = input("Enter the phone number of the contact to delete: ").strip()

    # Locate the contact using the phone number
    matched_contact = next((contact for contact in contacts if contact['phone'] == search_phone), None)

    if not matched_contact:
        print("No contact found with the given phone number.")
        return

    print(f"\nFound Contact: Name: {matched_contact['name']}, "
          f"Phone: {matched_contact['phone']}, Email: {matched_contact['email']}, "
          f"Address: {matched_contact['address']}")

    # Confirm deletion
    confirm = input("Are you sure you want to delete this contact? (yes/no): ").strip().lower()
    if confirm == 'yes':
        contacts.remove(matched_contact)
        file_manager.save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Deletion canceled.")



def search_contacts():
    query = input("Enter search query (name, phone, email, or address): ").strip().lower()
    results = [contact for contact in contacts if query in contact['name'].lower() or
               query in contact['phone'] or
               query in contact['email'].lower() or
               query in contact['address'].lower()]
    if results:
        print("\n--- Search Results ---")
        for idx, contact in enumerate(results, start=1):
            print(f"{idx}. Name: {contact['name']}, Phone: {contact['phone']}, "
                  f"Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.")

