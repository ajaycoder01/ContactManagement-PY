import json
import os
import re


FILE_NAME = "contacts.json"


# --------------------------------------------------
# File Handling
# --------------------------------------------------

def load_contacts():
    """Load contacts from JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# --------------------------------------------------
# Validation
# --------------------------------------------------

def validate_phone(phone):
    """
    Validates a 10-digit Indian phone number.
    Example: 9876543210
    """
    pattern = r"^[6-9]\d{9}$"
    return re.fullmatch(pattern, phone) is not None


def validate_email(email):
    """Validate email address."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.fullmatch(pattern, email) is not None


# --------------------------------------------------
# Duplicate Detection
# --------------------------------------------------

def is_duplicate(contacts, phone, email, ignore_id=None):
    """
    Check whether phone number or email already exists.

    ignore_id is used while updating a contact so that
    the contact's own phone/email is not treated as duplicate.
    """

    for contact in contacts:

        if contact["id"] == ignore_id:
            continue

        if contact["phone"] == phone:
            return "phone"

        if contact["email"].lower() == email.lower():
            return "email"

    return None


# --------------------------------------------------
# Display Contact
# --------------------------------------------------

def display_contact(contact):
    """Display one contact."""
    print("-" * 40)
    print(f"ID       : {contact['id']}")
    print(f"Name     : {contact['name']}")
    print(f"Phone    : {contact['phone']}")
    print(f"Email    : {contact['email']}")
    print(f"Category : {contact['category']}")
    print("-" * 40)


# --------------------------------------------------
# Add Contact
# --------------------------------------------------

def add_contact(contacts):
    print("\n===== Add Contact =====")

    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    # Phone validation
    while True:
        phone = input("Enter phone number: ").strip()

        if validate_phone(phone):
            break

        print("Invalid phone number.")
        print("Please enter a valid 10-digit Indian mobile number.")

    # Email validation
    while True:
        email = input("Enter email: ").strip()

        if validate_email(email):
            break

        print("Invalid email address.")
        print("Example: abc@gmail.com")

    category = input(
        "Enter category (Family/Friends/Work/Other): "
    ).strip()

    if not category:
        category = "Other"

    # Duplicate check
    duplicate = is_duplicate(contacts, phone, email)

    if duplicate == "phone":
        print("Contact already exists with this phone number.")
        return

    if duplicate == "email":
        print("Contact already exists with this email.")
        return

    # Generate ID
    if contacts:
        new_id = max(contact["id"] for contact in contacts) + 1
    else:
        new_id = 1

    new_contact = {
        "id": new_id,
        "name": name,
        "phone": phone,
        "email": email,
        "category": category
    }

    contacts.append(new_contact)
    save_contacts(contacts)

    print("Contact added successfully.")


# --------------------------------------------------
# View All Contacts
# --------------------------------------------------

def view_contacts(contacts):
    print("\n===== All Contacts =====")

    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        display_contact(contact)


# --------------------------------------------------
# Search Contacts
# --------------------------------------------------

def search_contacts(contacts):
    print("\n===== Search Contacts =====")

    if not contacts:
        print("No contacts found.")
        return

    keyword = input(
        "Search by name, phone, email or category: "
    ).strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    results = []

    for contact in contacts:

        if (
            keyword in contact["name"].lower()
            or keyword in contact["phone"]
            or keyword in contact["email"].lower()
            or keyword in contact["category"].lower()
        ):
            results.append(contact)

    if not results:
        print("No matching contacts found.")
        return

    print(f"\n{len(results)} contact(s) found.")

    for contact in results:
        display_contact(contact)


# --------------------------------------------------
# Filter by Category
# --------------------------------------------------

def filter_contacts(contacts):
    print("\n===== Filter Contacts =====")

    if not contacts:
        print("No contacts found.")
        return

    category = input(
        "Enter category (Family/Friends/Work/Other): "
    ).strip().lower()

    results = []

    for contact in contacts:
        if contact["category"].lower() == category:
            results.append(contact)

    if not results:
        print("No contacts found in this category.")
        return

    print(f"\nContacts in '{category.title()}':")

    for contact in results:
        display_contact(contact)


# --------------------------------------------------
# Find Contact by ID
# --------------------------------------------------

def find_contact(contacts, contact_id):
    """Find contact using ID."""
    for contact in contacts:
        if contact["id"] == contact_id:
            return contact

    return None


# --------------------------------------------------
# Update Contact
# --------------------------------------------------

def update_contact(contacts):
    print("\n===== Update Contact =====")

    if not contacts:
        print("No contacts found.")
        return

    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    contact = find_contact(contacts, contact_id)

    if contact is None:
        print("Contact not found.")
        return

    print("\nCurrent contact:")
    display_contact(contact)

    print("\nEnter new details.")

    # Name
    name = input(
        f"Enter new name [{contact['name']}]: "
    ).strip()

    if not name:
        name = contact["name"]

    # Phone
    while True:
        phone = input(
            f"Enter new phone [{contact['phone']}]: "
        ).strip()

        if not phone:
            phone = contact["phone"]

        if validate_phone(phone):
            break

        print("Invalid phone number.")
        print("Please enter a valid 10-digit Indian mobile number.")

    # Email
    while True:
        email = input(
            f"Enter new email [{contact['email']}]: "
        ).strip()

        if not email:
            email = contact["email"]

        if validate_email(email):
            break

        print("Invalid email address.")

    # Category
    category = input(
        f"Enter new category [{contact['category']}]: "
    ).strip()

    if not category:
        category = contact["category"]

    # Duplicate check
    duplicate = is_duplicate(
        contacts,
        phone,
        email,
        ignore_id=contact_id
    )

    if duplicate == "phone":
        print("Another contact already has this phone number.")
        return

    if duplicate == "email":
        print("Another contact already has this email.")
        return

    # Update contact
    contact["name"] = name
    contact["phone"] = phone
    contact["email"] = email
    contact["category"] = category

    save_contacts(contacts)

    print("Contact updated successfully.")


# --------------------------------------------------
# Delete Contact
# --------------------------------------------------

def delete_contact(contacts):
    print("\n===== Delete Contact =====")

    if not contacts:
        print("No contacts found.")
        return

    try:
        contact_id = int(input("Enter contact ID: "))
    except ValueError:
        print("Please enter a valid ID.")
        return

    contact = find_contact(contacts, contact_id)

    if contact is None:
        print("Contact not found.")
        return

    display_contact(contact)

    confirmation = input(
        "Are you sure you want to delete this contact? (y/n): "
    ).strip().lower()

    if confirmation == "y":
        contacts.remove(contact)
        save_contacts(contacts)
        print("Contact deleted successfully.")
    else:
        print("Delete operation cancelled.")


# --------------------------------------------------
# Main Menu
# --------------------------------------------------

def main():
    contacts = load_contacts()

    while True:

        print("\n")
        print("=" * 45)
        print("       CONTACT MANAGEMENT SYSTEM")
        print("=" * 45)

        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Filter by Category")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            view_contacts(contacts)

        elif choice == "3":
            search_contacts(contacts)

        elif choice == "4":
            filter_contacts(contacts)

        elif choice == "5":
            update_contact(contacts)

        elif choice == "6":
            delete_contact(contacts)

        elif choice == "7":
            print("\nThank you for using Contact Management System.")
            break

        else:
            print("Invalid choice. Please select 1-7.")


# --------------------------------------------------
# Program Start
# --------------------------------------------------

if __name__ == "__main__":
    main()
