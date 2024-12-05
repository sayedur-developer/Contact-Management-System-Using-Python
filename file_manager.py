import csv

FILE_NAME = "contacts.csv"

def save_contacts(contact_list):
    try:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "email", "address"])
            writer.writeheader()
            writer.writerows(contact_list)
    except Exception as e:
        print(f"Error saving contacts: {e}")

def load_contacts():
    contact_list = []
    try:
        with open(FILE_NAME, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact_list.append(row)
    except FileNotFoundError:
        print("No existing contact file found. A new one will be created.")
    except Exception as e:
        print(f"Error loading contacts: {e}")
    return contact_list
