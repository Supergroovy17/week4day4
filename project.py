
import re
import os

def display_menu():
    print('Welcome to Pandora')
    print('''
    1. Add a new contact
    2. Edit an existing contact   
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file
    8. Quit 
   
    ''')
def write_contacts(contacts, filename='the_contact.txt'):
    with open(filename, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['Name']}|o|{contact['Phone Number']}|o|{contact['Email']}|o|\n")

def read_contacts(filename='the_contact.txt'):
    contacts = []
    with open(filename, 'r') as file:
        for line in file:
            name, phone, email = line.strip().split('|o|')
            contacts.append({'Name': name, 'Phone Number': phone, 'Email': email})
    return contacts

def add_contact(contacts):
    os.system('cls' if os.name == 'nt' else 'clear')
    name = input('Name: ')
    phone_number = input('Phone Number: ')
    email = input('Email: ')
    contacts.append({'Name': name, 'Phone Number': phone_number, 'Email': email})
    write_contacts(contacts)
    print(f'Added {name} to your list!')

def edit_contact(contacts):
    replace_me = input('What would you like to replace: ')
    for contact in contacts:
        if replace_me == contact['Name']:
            print("What would you like to edit?")
            print("1. Name")
            print("2. Phone Number")
            print("3. Email")
            choice = input("Enter your choice: ")
            if choice == "1":
                new_name = input('Enter the new name: ')
                contact['Name'] = new_name
                print(f'{replace_me} replaced with {new_name} successfully!')
            elif choice == "2":
                new_phone = input('Enter the new phone number: ')
                contact['Phone Number'] = new_phone
                print(f'Phone number updated successfully!')
            elif choice == "3":
                new_email = input('Enter the new email address: ')
                contact['Email'] = new_email
                print(f'Email address updated successfully!')
            else:
                print('Invalid choice!')
            write_contacts(contacts)
            return
    print(f'Contact {replace_me} not found!')

def delete_contact(contacts):
    delete_me = input('What item do you want to remove? ')
    for contact in contacts:
        if delete_me == contact['Name']:
            contacts.remove(contact)
            print(f"{contact['Name']} has been removed from the list.")
            display_menu()
            return
    print(f'Contact {delete_me} not found!')

def search_contact(contacts):
    search_term = input('Enter the name of the contact you want to search: ')
    for contact in contacts:
        if search_term == contact['Name']:
            print('Contact found:')
            print(contact)
            return
    print(f'Contact {search_term} not found!')

def display_all_contacts(contacts):
    for contact in contacts:
        print(contact)

def export_contacts(contacts):
    filename = input("Enter the filename to export to: ")
    write_contacts(contacts, filename)
    print("Contacts exported successfully!")

def import_contacts(contacts):
    filename = input("Enter the filename to import from: ")
    contacts.extend(read_contacts(filename))
    print("Contacts imported successfully!")

def quit_program():
    print('Goodbye!')

def main():
    contacts = []
    while True:
        display_menu()
        choice = input('Enter your choice: ')
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_all_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts)
        elif choice == '7':
            import_contacts(contacts)
        elif choice == '8':
            quit_program()
            break
        else:
            print('Invalid choice!')

if __name__ == '__main__':
    main()