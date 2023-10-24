import sqlite3

# Define the Contact and ContactList classes as before.
class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("contacts.db")
        self.create_table()

    def create_table(self):
        c = self.conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                phone_number TEXT,
                email TEXT,
                address TEXT
            )
        ''')
        self.conn.commit()

    def add_contact(self, contact):
        c = self.conn.cursor()
        c.execute('''
            INSERT INTO contacts (name, phone_number, email, address)
            VALUES (?, ?, ?, ?)
        ''', (contact.name, contact.phone_number, contact.email, contact.address))
        self.conn.commit()

    def get_all_contacts(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM contacts")
        return c.fetchall()

    def search_contacts(self, keyword):
        c = self.conn.cursor()
        c.execute('''
            SELECT * FROM contacts
            WHERE name LIKE ? OR phone_number LIKE ?
        ''', (f"%{keyword}%", f"%{keyword}%"))
        return c.fetchall()

    def update_contact(self, contact_id, updated_contact):
        c = self.conn.cursor()
        c.execute('''
            UPDATE contacts
            SET name = ?, phone_number = ?, email = ?, address = ?
            WHERE id = ?
        ''', (updated_contact.name, updated_contact.phone_number, updated_contact.email, updated_contact.address, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        c = self.conn.cursor()
        c.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

def main():
    db = Database()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")
        
        choice = input("Select an option (1/2/3/4/5/6): ")
        
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")
            new_contact = Contact(name, phone, email, address)
            db.add_contact(new_contact)
            print("Contact added successfully.")
        
        elif choice == "2":
            contacts = db.get_all_contacts()
            for i, contact in enumerate(contacts, start=1):
                print(f"{i}. Name: {contact[1]}, Phone: {contact[2]} , Email: {contact[3]}, Address: {contact[4]}")
        
        elif choice == "3":
            keyword = input("Enter a name or phone number to search: ")
            results = db.search_contacts(keyword)
            if results:
                for i, contact in enumerate(results, start=1):
                    print(f"{i}. Name: {contact[1]}, Phone: {contact[2]}")
            else:
                print("No matching contacts found.")
        
        elif choice == "4":
            index = int(input("Enter the index of the contact to update: "))
            name = input("Name: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            address = input("Address: ")
            updated_contact = Contact(name, phone, email, address)
            db.update_contact(contacts[index - 1][0], updated_contact)
        
        elif choice == "5":
            index = int(input("Enter the index of the contact to delete: "))
            db.delete_contact(contacts[index - 1][0])
        
        elif choice == "6":
            print("Goodbye!")
            db.close()
            break

if __name__ == "__main__":
    main()
