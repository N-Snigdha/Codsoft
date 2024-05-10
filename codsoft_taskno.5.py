class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for i, contact in enumerate(self.contacts):
                print(f"{i + 1}. Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print("No contacts in the contact book.")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s) with the name '{name}':")
            for contact in found_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}, Address: {contact.address}")
        else:
            print(f"No contact found with the name '{name}'.")

    def update_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                new_name = input("Enter new name (leave blank to keep current): ")
                new_phone_number = input("Enter new phone number (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_address = input("Enter new address (leave blank to keep current): ")
                if new_name.strip():
                    contact.name = new_name
                if new_phone_number.strip():
                    contact.phone_number = new_phone_number
                if new_email.strip():
                    contact.email = new_email
                if new_address.strip():
                    contact.address = new_address
                print("Contact updated successfully.")
                return
        print(f"No contact found with the name '{name}'.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print(f"No contact found with the name '{name}'.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone_number, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == "2":
            contact_book.display_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            contact_book.search_contact(name)
        elif choice == "4":
            name = input("Enter name of contact to update: ")
            contact_book.update_contact(name)
        elif choice == "5":
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
