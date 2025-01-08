import re

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\n--- Contact List ---")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")
        print("---------------------")

    def search_contact(self, query):
        found = False
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print(f"Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, Address: {contact.address}")
                found = True
        if not found:
            print("No contact found with that query.")

    def update_contact(self, name, new_contact):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[i] = new_contact
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def validate_phone(self, phone):
        """Basic phone validation: Should be digits and at least 10 characters long"""
        return phone.isdigit() and len(phone) >= 10

    def validate_email(self, email):
        """Basic email validation"""
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email)

def main():
    manager = ContactManager()

    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")

            while not manager.validate_phone(phone):
                print("Invalid phone number. Please enter a valid phone number (10 digits minimum).")
                phone = input("Enter phone number: ")

            email = input("Enter email: ")
            while not manager.validate_email(email):
                print("Invalid email. Please enter a valid email address.")
                email = input("Enter email: ")

            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            manager.add_contact(contact)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            manager.search_contact(query)

        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")

            while not manager.validate_phone(new_phone):
                print("Invalid phone number. Please enter a valid phone number (10 digits minimum).")
                new_phone = input("Enter new phone number: ")

            new_email = input("Enter new email: ")
            while not manager.validate_email(new_email):
                print("Invalid email. Please enter a valid email address.")
                new_email = input("Enter new email: ")

            new_address = input("Enter new address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            manager.update_contact(name, new_contact)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print(" Thanks for using the Application , Exiting the Contact Manager. ")
if __name__ == "__main__":
    main()
